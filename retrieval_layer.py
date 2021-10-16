import requests 
import pandas as pd
from datetime import datetime
from API_wrapper import NSEAPIs
from bs4 import BeautifulSoup
from functools import wraps
from exceptions import IllegalArgumentError, DataNotFound

class Retrieve:

    def __init__(self) -> None:
        self.api_url = NSEAPIs()
        self.stock_symbols = self.get_stock_symbols()

    def get_stock_symbols(self) -> dict:
        df = pd.read_csv("stocksymbols.csv")
        stock_symbols = {}
        for i,row in df.iterrows():
            stock_symbols[row["nse"]] = row["nse"].replace("&", "%26")
            if pd.isna(row["bse"]) == False:
                stock_symbols[str(int(row["bse"]))] = row["nse"]
        return stock_symbols

    def date_validation(f) -> any:
        @wraps(f)
        def validate(*args, **kwargs):
            from_date = datetime.strptime(args[2],"%d-%m-%Y")
            to_date = datetime.strptime(args[3],"%d-%m-%Y")
            if from_date > to_date:
                raise IllegalArgumentError("From Date('from_date') must be smaller than To Date('to_date')")
            return f(*args,**kwargs)
        return validate

    def convert_to_df(self,stock_arr) -> pd.DataFrame:
        cols = stock_arr[0].split(",")
        stock_arr = [rec.replace(" ","").replace("\"","").split(",") for rec in stock_arr[1:-1]] 
        data = {}
        for i in range(len(cols)):
            data[cols[i]] = [float(r[i]) if r[i].isdigit() else r[i] for r in stock_arr]
        return pd.DataFrame(data)

    def extract_data(self,html) -> pd.DataFrame:
        try:
            return self.convert_to_df(BeautifulSoup(html, "html.parser").find(id="csvContentDiv").get_text().replace("\"","").split(":"))
        except AttributeError as e:
            raise DataNotFound("Data For this stock Not found")

    @date_validation
    def stock_data(self, symbol, from_date, to_date, params=None) -> pd.DataFrame:
        if self.stock_symbols.get(symbol) is not None:
            symbol = self.stock_symbols[symbol]
            url = self.api_url.stock_data.format(symbol, from_date, to_date)
            headers = self.api_url.header
            res = requests.get(url,headers=headers)
            if res.status_code == 200:
                return self.extract_data(res.text)
            raise DataNotFound("Data For this stock Not found")
        else:
            raise DataNotFound("Stock Symbol not Found: Check Stock symbol")

    def historical_stock_data(self, symbol, from_date, to_date,params=None):
        url = self.api_url.historical_stock_data.format(symbol, from_date, to_date)
        res = requests.get(url, headers=self.api_url.stock_header)
        return res.json()
    

