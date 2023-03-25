
# About the Project
Easy_klines is a Python library that provides a simple and efficient solution for retrieving historical candlestick data from exchange APIs.

The library overcomes the limitations of exchange APIs, such as rate limits and inefficient data retrieval, by providing a unified interface for accessing candlestick data across multiple exchanges. It currently supports Binance, Bybit, and Oanda exchanges.

Easy_klines allows you to easily retrieve historical candlestick data for a specific symbol and timefram.

# Installation
You can install Easy_klines using pip:


```

pip install easy-kline


```


# How to Use Easy_klines


First, import the Easy_klines library:

```
import easy_kline
```


Then, you can retrieve candlestick data from different exchanges, such as Binance, Bybit, or Oanda, using the exchange method:

symbol: the symbol of the cryptocurrency that you want to retrieve the data for. For example, 'BTCUSDT' or 'ETHUSDT' for banance and bybit, 'BTC_USD' or 'EUR_USD' for oanda.

timeframe: the timeframe for the candlestick data. For example, '1h' for one-hour intervals or '5m' for five-minute intervals.
valid timeframes ['1m', '3m', '5m','15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h' '1d', '1w']

start_time: the start time for the data in the format 'YYYY-MM-DD HH:MM'. The output of the library is from start_time until the current time.







```python
# binance

kline = easy_kline.exchange('BTCUSDT', '1h', '2023-01-20 12:00')
BTCUSDT = kline.binance()
print(BTCUSDT)


# bybit
 
kline = easy_kline.exchange('ETHUSDT', '2h', '2022-06-25 11:00')
ETHUSDT = kline.bybit()
print(BTCUSDT)


# oanda

kline = easy_kline.exchange('EUR_USD', '5m', '2023-01-13 9:00')
BTC_USD = kline.oanda()
print(BTCUSDT)

```

# License

This project is distributed under the MIT License. See the LICENSE.txt file for more information.




# Contact

You can contact the author, mohder, at mohder1379@gmail.com.

#Links 

GitHub Repository: https://github.com/mohder79/Easy_klines
PyPI Page: https://pypi.org/project/easy-kline/
