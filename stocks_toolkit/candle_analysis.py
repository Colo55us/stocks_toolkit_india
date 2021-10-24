import talib
from .retrieval_layer import Retrieve
import pandas as pd

class Candle_analysis:

    def __init__(self) -> None:
        self.retrieve_stocks = Retrieve()

    def candle_patterns(self) -> list:
        return talib.get_function_groups()['Pattern Recognition']

    def filter_technicals(self,df) -> pd.DataFrame:
        return pd.DataFrame({"open":list(df["Open Price"]), "close":list(df["Close Price"]), "high":list(df["High Price"]), "low":list(df["Low Price"]),"date":list(df["Date"])})

    def find_candles(self, symbol, from_date, to_date) -> pd.DataFrame:
        data = self.filter_technicals(self.retrieve_stocks.stock_data(symbol, from_date, to_date))
        candles_found = [[] for _ in range(len(data))]
        for candle in self.candle_patterns():
            candle_weights = getattr(talib,candle)(data["open"],data["high"],data["low"],data["close"])
            for i in range(len(candle_weights)):
                if candle_weights[i] == 100:
                    candles_found[i].append(candle+":Bullish")
                elif candle_weights[i] == -100:
                    candles_found[i].append(candle+":Bearish")
        data["candles_found"] = candles_found
        return data
