import requests
import pandas as pd


class bybit():
    def __init__(self, exchange_name, symbol, time_frame, start_time):
        self.exchange_name = exchange_name
        self.symbol = symbol
        self.timeframe = time_frame
        self.start_time = start_time

    def bybit(self):

        url = f'https://api.bybit.com/v5/market/kline?category=inverse&symbol=BTCUSD&interval=60&start=1670601600000'

        response = requests.get(url)
        data = response.json()['result']['list']
        data = [i[:-1] for i in data]
        df = pd.DataFrame(data)
        df.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']

        return df
