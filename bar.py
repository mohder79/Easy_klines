# test
import time
import pytz
import ccxt
from datetime import timedelta
import pandas as pd
import re
import requests
import json
import re
import dateutil.tz
import datetime
import pytz
# import bybit  # test

pd.set_option('display.max_rows', None)  # fix *** to show all rows

# from configs import API_KEY, ACCOUNT_ID, HEADERS, INSTRUMENT, GRANULARITY, FAST, SLOW, BUY, SELL
# bybit = bybit.Bybit_ex()
# Bybit_ex.data()


class TimeFrameErore(Exception):
    pass


class Data:
    def __init__(self,  symbol, time_frame, start_time):

        self.symbol = symbol
        self.timeframe = time_frame
        self.start_time = start_time

    def date_time_to_timestamp(self):

        est_timezone = pytz.timezone('UTC')
        time_obj = datetime.datetime.strptime(
            self.start_time, '%Y-%m-%d %H:%M').replace(tzinfo=est_timezone)
        timestamp = int(time_obj.timestamp())
        return timestamp * 1000

    def timeframe_check(self, data):
        time_frames_list = ['1m', '3m', '5m',
                            '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h' '1d', '1w']
        if self.timeframe not in time_frames_list:
            raise TimeFrameErore(
                f'"wrong timeframe" timeframe must like : {time_frames_list} ')

    def timeframe_converter(self):
        time = self.timeframe
        times = {'1m': 1, '3m': 3, '5m': 5, '15m': 15, '30': 30, '1h': 60,
                 '2h': 120, '4h': 240, '6h': 360, '8h': 480, '12h': 720, '1d': 1440, '1w': 10080}
        return times.get(time)

    def get_bar(self, data):
        self.timeframe_check(data)
        arguments = self.symbol, self.timeframe, self.start_time
        print(data)
        exchanges = {'bybit': Bybit,
                     'binance': Binance}.get(data)
        if exchanges is None:
            # handle invalid data parameter
            pass
        print(exchanges)
        exchange = exchanges(*arguments)
        print(exchange)
        bars = exchange.bybit_data() if data == 'bybit' else exchange.binance_data(
        ) if data == 'binance' else self.coinex_data() if data == 'coinex' else None

        print(bars)

        print(f'Fetching {self.symbol} new bar for {self.start_time}')

        while True:

            last_time = bars['Time'].iloc[-1]
            print(last_time)
            # for test
            last_row_mask = bars.index == (len(bars) - 1)
            bars.loc[last_row_mask,
                     'volume'] = 'XXXXXXXXSSSSAAAAAZZZZZZXXXXX'
            #
            time_now = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M')
            time = self.timeframe_converter()
            time_format = "%Y-%m-%d %H:%M"
            time1 = datetime.datetime.strptime(time_now, time_format)
            time2 = datetime.datetime.strptime(last_time, time_format)

            difference_in_minutes = (time1 - time2).total_seconds() // 60
            if difference_in_minutes <= time:
                break
            else:

                last_bar_datetime = datetime.datetime.strptime(
                    last_time, '%Y-%m-%d %H:%M')
                new_time = (
                    last_bar_datetime + timedelta(minutes=time)).strftime('%Y-%m-%d %H:%M')

                self.start_time = new_time
                arguments = self.symbol, self.timeframe, self.start_time
                exchange = exchanges(*arguments)

                bar2 = exchange.bybit_data() if data == 'bybit' else exchange.binance_data(
                ) if data == 'binance' else None
                print('vvvv')
                bars = pd.concat([bars, bar2]).reset_index(drop=True)
                last_row_mask = bars.index == (len(bars) - 1)
                bars.loc[last_row_mask,
                         'volume'] = 'XXXXXXXXXXXXX'
        bars.drop(bars.index[-1], inplace=True)

        return bars

    def binance(self):

        data = self.get_bar('binance')
        # data = self.get_bar()

        return data

    def bybit(self):

        data = self.get_bar('bybit')
        # data = self.get_bar()

        return data

    def coinex_perpetual_symbol(self):
        url = 'https://api.coinex.com/perpetual/v1/market/list'
        response = requests.get(url)
        data = response.json()['data']
        name = []
        for item in data:
            name.append(item['name'])

        data = pd.DataFrame(name, columns=['symbol'])

        return data

# {Bybit exchange


class Oanda():
    def __init__(self,  symbol, time_frame, start_time):
        super().__init__(symbol, time_frame, start_time)

    def oanda_timeframe(self):
        timeframe = self.timeframe
        bybit_timeframe = {'1m': 'M1', '3m': 'M3', '5m': 'M5', '15m': 'M15', '30': 'M30', '1h': 'H1',
                           '2h': 'H2', '4h': 'H4', '6h': 'H6', '8h': 'H8', '12h': 'H12', '1d': 'D', '1w': 'W'}
        return bybit_timeframe.get(timeframe)

    def oanda(self, API_KEY):
        API_KEY = API_KEY  # '393dc3deec6d2a0f20e328ee40e86595-b3810e7fcb6fafbab913519db3f51b2b'
        HEADERS = {
            'Authorization': 'Bearer ' + API_KEY
        }

        INSTRUMENT = 'EUR_USD'
        GRANULARITY = 'M1'
        print(int(self.date_time_to_timestamp()/1000))

        url = f"https://api-fxpractice.oanda.com/v3/instruments/{INSTRUMENT}/candles?count=5&price=M&granularity=M1"

        response = requests.get(url, headers=HEADERS).json()['candles']
        print(response)
        data = []
        for i in response:
            dtt = datetime.datetime.strptime(
                i['time'][:-4], '%Y-%m-%dT%H:%M:%S.%f')
            time = dtt.strftime('%Y-%m-%d %H:%M')
            data.append({'time': time, 'o': i['mid']['o'], 'h': i['mid']['h'], 'l': i['mid']
                        ['l'], 'c': i['mid']['c'], 'volume': i['volume']})
        df = pd.DataFrame(data)
        df.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']

        return df


class Binance(Data):

    def __init__(self,  symbol, time_frame, start_time):
        super().__init__(symbol, time_frame, start_time)

    def binance_data(self):
        url = f'https://api.binance.com/api/v3/klines?symbol={self.symbol}&interval={self.timeframe}&startTime={self.date_time_to_timestamp()}'

        response = requests.get(url)
        data = response.json()
        data = [i[:-6] for i in data]
        df = pd.DataFrame(
            data, columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume'])
        df['Time'] = pd.to_datetime(df['Time'], unit='ms', utc=True)
        # local_tz = pytz.timezone('Asia/Tehran')
        # df['Time'] = df['Time'].dt.tz_convert(local_tz)
        df['Time'] = df['Time'].dt.strftime('%Y-%m-%d %H:%M')

        return df


class Bybit(Data):

    def __init__(self,  symbol, time_frame, start_time):
        super().__init__(symbol, time_frame, start_time)

    # "The Bybit exchange has a different timeframe input compared to the input of my main program."
    def bybit_timeframe(self):
        timeframe = self.timeframe
        bybit_timeframe = {'1m': 1, '3m': 3, '5m': 5, '15m': 15, '30': 30, '1h': 60,
                           '2h': 120, '4h': 240, '6h': 360, '8h': 480, '12h': 720, '1d': 'D', '1w': 'W'}
        return bybit_timeframe.get(timeframe)

    def bybit_data(self):
        # TODO timeframe 1 , 3, 5 ,60

        url = f'https://api.bybit.com/v5/market/kline?category=inverse&symbol={self.symbol}&interval={self.bybit_timeframe()}&start={self.date_time_to_timestamp()}'

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
        df = df.reset_index(drop=True)

        return df


# 1675288344
# '2023-03-14 08:00'
data = Data('BTCUSD', '2h', '2023-01-15 11:00')
# 1670601600000
# 1672574400000
# 1636602204
print('bars')
bars = data.bybit()

# bars = data.oanda(
#     '393dc3deec6d2a0f20e328ee40e86595-b3810e7fcb6fafbab913519db3f51b2b')
# df = pd.DataFrame(bars)


print(bars)
# TODO bybit time is timestamp . get timestamp and timeframe method is 1m
# TODO binance time is timestamp . get time stamp timeframe method  1m
# TODO coinex time is timestamp but lower   get time stamp timeframe method  1min its defrent
