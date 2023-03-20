import requests
from datetime_to_timestamp import date_time_to_timestamp


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
