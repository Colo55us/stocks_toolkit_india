from retrieval_layer import Retrieve
from candle_analysis import Candle_analysis
from helper import Helper
from pandas import DataFrame

class stocks_toolkit:

    def __init__(self) -> None:    
        self.retrieve = Retrieve()
        self.ca = Candle_analysis()
        self.helper = Helper()

    def technical_data(self, symbol, from_date, to_date) -> DataFrame:
        return self.retrieve.stock_data(self, symbol, from_date, to_date)
    
    def candle_analysis(self, symbol, from_date, to_date) -> DataFrame:
        return self.ca.find_candles(self, symbol, from_date, to_date)

    def bse_to_nse(self, symbol) -> str:
        return self.helper.bse_to_nse(symbol)
    
    def nse_to_bse(self, symbol) -> str:
        return self.helper.nse_to_bse(symbol)

