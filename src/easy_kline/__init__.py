"""
easy_kline - A Python library for retrieving candlestick data from exchanges.
"""

__version__ = "0.0.2"
__author__ = "Mohder"

from .easy_klines import exchange


__all__ = ['Easy_Klines']
# from Easy_Klines import Easy_Klines
# data = Easy_Klines.Easy_Klines('BTCUSDT', '1h', '2023-01-20 12:00')

# bars = data.bybit()


# print(bars)
