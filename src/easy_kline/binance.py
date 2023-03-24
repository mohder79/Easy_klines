'''
This class retrieve data from the binance API. The class constructor takes four arguments: symbol, time_frame, start_time, and retry_count
The class has two methods: "binance_timeframe" and "binance_data".
The "binance_timeframe" method maps the time frame string to the corresponding string used by the binance API. 
The "binance_data" method sends a request to the binance API using the provided arguments to retrieve candlestick data for the specified symbol and time frame.
'''

import requests
from .datetime_to_timestamp import date_time_to_timestamp


class Binance():

    def __init__(self,  symbol, time_frame, start_time, retry_count: int = 5):

        self.symbol = symbol
        self.timeframe = time_frame
        self.start_time = start_time
        self.retry_count = retry_count

    def binance_data(self):
        url = f'https://api.binance.com/api/v3/klines?symbol={self.symbol}&interval={self.timeframe}&startTime={date_time_to_timestamp(self.start_time)}'

        response = requests.get(url)

        return response
