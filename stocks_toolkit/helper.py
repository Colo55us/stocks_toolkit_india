import pandas as pd
from .exceptions import DataNotFound
import pathlib

class Helper:

    def __init__(self) -> None:
        self.nse_bse, self.bse_nse = self.fetch_symbols()    

    def fetch_symbols(self) -> tuple:
        HERE = pathlib.Path(__file__).parent
        df = pd.read_csv(str(HERE)+str("\stocksymbols.csv"))
        nse_bse = {}
        bse_nse = {}
        for i,row in df.iterrows():
            if pd.isna(row["bse"]) == False:
                nse_bse[row["nse"]] = str(int(row["bse"]))
                bse_nse[str(int(row["bse"]))] = row["nse"]
        return nse_bse, bse_nse

    def bse_to_nse(self,symbol) -> str:
        if self.bse_nse.get(str(symbol)):
            return self.bse_nse[str(symbol)]
        else:
            raise DataNotFound("NSE symbol not found for this BSE symbol")
    
    def nse_to_bse(self,symbol) -> str:
        if self.nse_bse.get(str(symbol)):
            return self.nse_bse[str(symbol)]
        else:
            raise DataNotFound("BSE symbol not found for this NSE symbol")
    


