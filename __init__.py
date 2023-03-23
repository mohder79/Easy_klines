import pandas as pd
from get_bar import Get_Bar


pd.set_option('display.max_rows', None)  # fix *** to show all rows


class Easy_klines:
    def __init__(self,  symbol, time_frame, start_time, retry_count: int = 5):

        self.symbol = symbol
        self.timeframe = time_frame
        self.start_time = start_time
        self.retry_count = retry_count

    def binance(self):
        arguments = self.symbol, self.timeframe, self.start_time
        bar = Get_Bar(*arguments)

        data = bar.get_bar('binance')

        return data

    def bybit(self):
        arguments = self.symbol, self.timeframe, self.start_time
        bar = Get_Bar(*arguments)
        data = bar.get_bar('bybit')

        return data

    def oanda(self):
        arguments = self.symbol, self.timeframe, self.start_time
        bar = Get_Bar(*arguments)

        data = bar.get_bar('oanda')

        return data


data = Easy_klines('BTCUSDT', '1h', '2023-01-20 11:00')

bars = data.bybit()


print(bars)
