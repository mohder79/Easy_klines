import requests
import pandas as pd
from bar import Data


class Bybit_ex():
    # def __init__(self, exchange_name, symbol, time_frame, start_time):
    #     self.exchange_name = exchange_name
    #     self.symbol = symbol
    #     self.timeframe = time_frame
    #     self.start_time = start_time

    def data(self):
        # TODO timeframe 1 , 3, 5 ,60

        url = f'https://api.bybit.com/v5/market/kline?category=inverse&symbol={self.symbol}&interval=120&start={self.date_time_to_timestamp()}'

        response = requests.get(url)
        data = response.json()['result']['list']
        data = [i[:-1] for i in data]
        df = pd.DataFrame(data)
        df.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
        df['Time'] = pd.to_datetime(df['Time'], unit='ms', utc=True)
        # local_tz = pytz.timezone('Asia/Tehran')
        # df['Time'] = df['Time'].dt.tz_convert(local_tz)
        df['Time'] = df['Time'].dt.strftime('%Y-%m-%d %H:%M')
        df = df.iloc[::-1]

        return df
