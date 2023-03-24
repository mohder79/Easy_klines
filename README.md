<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


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

‍‍‍```
# binance
kline = easy_kline.exchange('BTCUSDT', '1h', '2023-01-20 12:00')
BTCUSDT = kline.binance()
print(BTCUSDT)

```



```

# bybit
kline = easy_kline.exchange('BTCUSDT', '2h', '2022-06-25 11:00')
BTCUSDT = kline.bybit()
print(BTCUSDT)

```


```

# oanda
kline = easy_kline.exchange('BTC_USD', '5m', '2023-01-13 9:00')
BTCUSDT = kline.oanda()
print(BTCUSDT)

```


# License

This project is distributed under the MIT License. See the LICENSE.txt file for more information.




# Contact

You can contact the author, mohder, at mohder1379@gmail.com.

#Links 

GitHub Repository: https://github.com/mohder79/Easy_klines
PyPI Page: https://pypi.org/project/easy-kline/
