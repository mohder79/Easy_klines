
import requests
from datetime_to_timestamp import date_time_to_timestamp


class Oanda():
    def __init__(self,  symbol, time_frame, start_time, retry_count: int = 5):

        self.symbol = symbol
        self.timeframe = time_frame
        self.start_time = start_time
        self.retry_count = retry_count

    def oanda_timeframe(self):
        timeframe = self.timeframe
        bybit_timeframe = {'1m': 'M1', '3m': 'M3', '5m': 'M5', '15m': 'M15', '30': 'M30', '1h': 'H1',
                           '2h': 'H2', '4h': 'H4', '6h': 'H6', '8h': 'H8', '12h': 'H12', '1d': 'D', '1w': 'W'}
        return bybit_timeframe.get(timeframe)

    def oanda_data(self):
        API_KEY = '393dc3deec6d2a0f20e328ee40e86595-b3810e7fcb6fafbab913519db3f51b2b'
        HEADERS = {
            'Authorization': 'Bearer ' + API_KEY
        }

        url = f"https://api-fxpractice.oanda.com/v3/instruments/{self.symbol}/candles?price=M&granularity={self.oanda_timeframe()}&from={int(date_time_to_timestamp(self.start_time)/1000)}&count=5000"
        response = requests.get(url, headers=HEADERS)

        return response
