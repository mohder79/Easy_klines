<p align="center">

  ![build](https://img.shields.io/badge/build%20-passing-green)
  ![Supported Exchanges](https://img.shields.io/badge/exchanges-3-blue.svg)
  ![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)
  [![PyPI](https://img.shields.io/badge/pypi-0.1.0-orange)](https://pypi.org/project/easy-kline/)
  [![web](https://img.shields.io/badge/mohder-website-brightgreen)](https://mohder.com) 
  
</p>

# About the Project
Easy_klines is a Python library that provides a simple and efficient solution for retrieving historical candlestick data from exchange APIs and provides efficient solutions for streaming historical candlestick data.

The library overcomes the limitations of exchange APIs, such as rate limits and inefficient data retrieval, by providing a unified interface for accessing candlestick data across multiple exchanges. It currently supports Binance, Bybit, and Oanda exchanges.

Easy_klines allows you to easily retrieve historical candlestick data for a specific symbol and timefram.


### How does candlestick streaming work?

Candlestick streaming works by sending a request to the exchange server upon the closing of a candle in a specified timeframe. The server responds with the latest data, which is then appended to the previous data.

The easy_kline library also provides the ability to save the retrieved data to an Excel file. However, it's important not to edit or open the Excel file while running the program, as it may cause errors.

Note that the easy_kline.pickle file should never be deleted or edited.


# Installation
You can install Easy_klines using pip:


```python

pip install easy-kline


```


# How to Use Easy_klines

Easy_kline Library Arguments for Retrieving Cryptocurrency or Forex market historical Data 


symbol: the symbol of the cryptocurrency or forex market that you want to retrieve the data for.
        For example,'BTCUSDT' or 'ETHUSDT' for banance and bybit, 'EUR_USD' or 'CAD_JPY' for oanda.

timeframe: the timeframe for the candlestick data. For example, '1h' for one-hour intervals or '5m' for 
        five-minute intervals.
        valid timeframes ['1m', '3m', '5m','15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h' '1d', '1w']

start_time: the start time for the data in the format 'YYYY-MM-DD HH:MM'. The output of the library is from 
        start_time until the current time.


futures : The futures parameter is a boolean value that determines whether the symbol being queried is a futures contract or a spot trading symbol. 
        If futures is set to False (which is the default), the function will fetch data for a spot trading symbol. 
        If futures is set to True, the function will fetch data for a futures trading symbol.

retry_count: The number of times the function will retry fetching data in case of a bad connection.
        The default value is set to 5.

auto_print: The auto_print parameter in the function is a boolean value that is False by default. 
        If auto_print is set to True, the data will be printed automatically without requiring any additional code to be written for printing.
        When auto_print is set to True, the data will be printed automatically as soon as it is fetched. 
        However, in streaming mode, only the last data point will be printed. 


## Binance Historical Data with Easy_kline

### Spot Trading Data

To retrieve historical data from Binance spot markets, use the following code:


```python
import easy_kline

# retrieve BTCUSDT spot trading data with 1-hour candlestick interval from 2023-01-20 12:00
BTCUSDT = easy_kline.binance('BTCUSDT', '1h', '2023-01-20 12:00') 

print(BTCUSDT)

```
### Futures Trading Data
To retrieve historical data from Binance futures markets, use the following code:


```python
import easy_kline

# retrieve SOLUSDT futures trading data with 2-hour candlestick interval from 2023-01-20 12:00
SOLUSDT = easy_kline.binance('SOLUSDT', '2h', '2023-01-20 12:00', futures=True) 

print(SOLUSDT)

```
### Streaming Data and Calculating SMA 
To stream real-time data from Binance futures markets and calculate the Simple Moving Average (SMA), use the following code:


```python
import easy_kline

# define function to calculate SMA
def SMA(data, length, column):
    return data[column].rolling(window=length).mean()

# retrieve ADAUSDT futures trading data with 2-hour candlestick interval from 2023-01-20 12:00
ADAUSDT = easy_kline.binance('ADAUSDT', '2h', '2023-01-20 12:00', futures=True)

# stream real-time data and calculate SMA
while True:
    ADAUSDT = easy_kline.stream()
    
    ADAUSDT['sma'] = SMA(ADAUSDT, 14, 'Close')
    print(ADAUSDT)

# Note that the easy_kline.stream() function will continue to stream data until the program is stopped.

```







# License

This project is distributed under the MIT License. See the LICENSE.txt file for more information.




# Contact

You can contact the author, mohder, at mohder1379@gmail.com.


#Links 


GitHub Repository: https://github.com/mohder79/Easy_klines

PyPI Page: https://pypi.org/project/easy-kline/
