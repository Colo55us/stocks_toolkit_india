## stocks_toolkit_india
Toolkit for NSE/BSE stocks comprises of various functionalities like historical technical data and candle pattern detection.

### To Install the package: 
>pip install stocks-toolkit-india


**Note**- This library needs TA-lib to be installed. To know more about how to install it  https://github.com/mrjbq7/ta-lib

**Note**- Functionality for Graph and better visualisation of data will be added.

**UPDATE** - NSE no more allows to get data more than 365 days. This library is designed to provide in depth analysis of recent trend pattern of a stock. 

#### For getting technical Data of a stock, the data is in pandas DataFrame Form.
```python 
from stock_toolkit import stock_toolkit
st = stock_toolkit()
stock_df = st.technical_data("INFY","01-01-2021","01-7-2021")
print(stock_df)
```
|    | Symbol   | Series   | Date        |   Prev Close |   Open Price |   High Price |   Low Price |   Last Price |   Close Price |   Average Price |   Total Traded Quantity |    Turnover |   No. of Trades |   Deliverable Qty |   % Dly Qt to Traded Qty |
|---:|:---------|:---------|:------------|-------------:|-------------:|-------------:|------------:|-------------:|--------------:|----------------:|------------------------:|------------:|----------------:|------------------:|-------------------------:|
|  0 | RELIANCE | EQ       | 01-Jan-2021 |      1985.3  |       1988   |       1997   |     1982    |      1988    |       1987.5  |         1989.5  |             4.622e+06   | 9.19548e+09 |          139680 |       1.01331e+06 |                    21.92 |
|  1 | RELIANCE | EQ       | 04-Jan-2021 |      1987.5  |       1995.1 |       1998.9 |     1968    |      1990.25 |       1990.85 |         1982.61 |             1.1313e+07  | 2.24292e+10 |          316871 |       3.8696e+06  |                    34.2  |
|  2 | RELIANCE | EQ       | 05-Jan-2021 |      1990.85 |       1969   |       1983.6 |     1956    |      1965    |       1966.1  |         1968.87 |             1.11328e+07 | 2.1919e+10  |          300233 |       5.20805e+06 |                    46.78 |
|  3 | RELIANCE | EQ       | 06-Jan-2021 |      1966.1  |       1965.9 |       1966   |     1905.15 |      1915.5  |       1914.25 |         1928.17 |             2.14143e+07 | 4.12904e+10 |          659284 |       9.0381e+06  |                    42.21 |
|  4 | RELIANCE | EQ       | 07-Jan-2021 |      1914.25 |       1920.5 |       1945   |     1905.15 |      1912.8  |       1911.15 |         1919.86 |             1.49184e+07 | 2.86413e+10 |          454695 |       6.45266e+06 |                    43.25 |
|  5 | RELIANCE | EQ       | 08-Jan-2021 |      1911.15 |       1918   |       1938.4 |     1912.1  |      1934    |       1933.7  |         1923.06 |             1.27098e+07 | 2.44418e+10 |          270966 |       5.30355e+06 |                    41.73 |



#### For getting the candle analysis, candle patter found in the stock:
```python
candles = st.candle_analysis("INFY","01-01-2021","01-7-2021")
print(candles)
```
|    |   open |   close |   high |     low | date        | candles_found   |
|---:|-------:|--------:|-------:|--------:|:------------|:----------------|
|  0 | 1988   | 1987.5  | 1997   | 1982    | 01-Jan-2021 | []              |
|  1 | 1995.1 | 1990.85 | 1998.9 | 1968    | 04-Jan-2021 | []              |
|  2 | 1969   | 1966.1  | 1983.6 | 1956    | 05-Jan-2021 | []              |
|  3 | 1965.9 | 1914.25 | 1966   | 1905.15 | 06-Jan-2021 | []              |
|  4 | 1920.5 | 1911.15 | 1945   | 1905.15 | 07-Jan-2021 | []              |
|  5 | 1918   | 1933.7  | 1938.4 | 1912.1  | 08-Jan-2021 | []              |
| .. |  ...   |   ...   |   ...  |   ...   |    ...      | ...             |
| 118 | 1572.00 |  1574.20 |  1578.00 |  1543.00 |  25-Jun-2021 | [CDLDOJI:Bullish, CDLDOJISTAR:Bearish, CDLLONG... |
| 119 | 1572.90 |  1571.80 |  1580.15 |  1560.60 |  28-Jun-2021 | [CDLDOJI:Bullish, CDLHIGHWAVE:Bearish, CDLLONG... |
| 120 | 1561.00 |  1563.05 |  1573.65 |  1559.20 |  29-Jun-2021 | [CDLDOJI:Bullish, CDLGRAVESTONEDOJI:Bullish, C... |
| 121 | 1572.05 |  1580.80 |  1591.00 |  1572.05 |  30-Jun-2021 |                         [CDLSHOOTINGSTAR:Bearish] |

                                      


The 'candles_found' column contains array of candle name along with their characterstics i.e Bullish/Bearish
>CDLGRAVESTONEDOJI:Bullish => Grave Stone Doji candle pattern indicating Bullish behavoiour.

Note - A single array can have candles indicating both Bearish and Bullish behavious. Read more about Japanese Candle stick patterns - https://www.nomuradirect.com/pdf/21_Candlesticks.pdf



##### Both NSE symbol and BSE symbol can be provided as symbol in both of the above functions. If the data is available with NSE, both of the function will return data.

#### To convert NSE symbol to bse symbol use:

```python
print(st.nse_to_bse("INFY")))
500209
```

#### and to convert bse symbol to nse symbol use:
```python
print(st.bse_to_nse("500325")))
RELIANCE
```
