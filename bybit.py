import requests
import pandas as pd
from datetime_to_timestamp import date_time_to_timestamp


class Bybit():

    def __init__(self,  symbol, time_frame, start_time, retry_count: int = 5):

        self.symbol = symbol
        self.timeframe = time_frame
        self.start_time = start_time
        self.retry_count = retry_count

    # "The Bybit exchange has a different timeframe input compared to the input of my main program."
    def bybit_timeframe(self):
        timeframe = self.timeframe
        bybit_timeframe = {'1m': 1, '3m': 3, '5m': 5, '15m': 15, '30': 30, '1h': 60,
                           '2h': 120, '4h': 240, '6h': 360, '8h': 480, '12h': 720, '1d': 'D', '1w': 'W'}
        return bybit_timeframe.get(timeframe)

    def bybit_data(self):

        url = f'https://api.bybit.com/v5/market/kline?category=inverse&symbol={self.symbol}&interval={self.bybit_timeframe()}&start={date_time_to_timestamp(self.start_time)}'

        response = requests.get(url)

        return response
