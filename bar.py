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
import sys
from bybit import Bybit
from binance import Binance
# import bybit  # test

pd.set_option('display.max_rows', None)  # fix *** to show all rows

# from configs import API_KEY, ACCOUNT_ID, HEADERS, INSTRUMENT, GRANULARITY, FAST, SLOW, BUY, SELL
# bybit = bybit.Bybit_ex()
# Bybit_ex.data()


class TimeFrameErore(Exception):
    pass


class Data:
    def __init__(self,  symbol, time_frame, start_time, retry_count: int = 5):

        self.symbol = symbol
        self.timeframe = time_frame
        self.start_time = start_time
        self.retry_count = retry_count

    def date_time_to_timestamp(self):

        est_timezone = pytz.timezone('UTC')
        time_obj = datetime.datetime.strptime(
            self.start_time, '%Y-%m-%d %H:%M').replace(tzinfo=est_timezone)
        timestamp = int(time_obj.timestamp())
        return timestamp * 1000

    def ــtimeframe_checkــ(self):
        time_frames_list = ['1m', '3m', '5m',
                            '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h' '1d', '1w']
        if self.timeframe not in time_frames_list:
            sys.exit(
                (f' Wrong timeframe! Timeframe must be one of: {time_frames_list}'))

    def __errors__(self, exchange_name, response):
        if exchange_name == 'bybit':
            response = response.json()['retCode']
        if exchange_name == 'bybit':
            if response == 10001:
                sys.exit(
                    ("\n Error Code 10001: Request parameter error. Invalid symbol."))

            if response == 10006:
                sys.exit(
                    ("\n Error Code 10006: Too many visits. Exceeded the API Rate Limit.."))

            if response == 10001:
                sys.exit(
                    ("\n Error Code 10009: IP has been banned."))
        if exchange_name == 'binance':
            if 'code' in response.json():

                response = response.json()['code']
                if response == -1121:

                    sys.exit(
                        ("\n Error Code -1121: Request parameter error. Invalid symbol."))

                if response == -1003 or -1121:
                    sys.exit(
                        ("\n Error Code -1003: Too many visits. Exceeded the API Rate Limit.."))
                if response == -1021:
                    sys.exit('INVALID_TIMESTAMP')

    def timeframe_converter(self):
        time = self.timeframe
        times = {'1m': 1, '3m': 3, '5m': 5, '15m': 15, '30': 30, '1h': 60,
                 '2h': 120, '4h': 240, '6h': 360, '8h': 480, '12h': 720, '1d': 1440, '1w': 10080}
        return times.get(time)

    def response_to_json(self, exchange_name: str, response):
        minus = {'bybit': -1, 'binance': -6, 'oanda': -4}.get(exchange_name)
        if exchange_name == 'bybit':
            data = response.json()['result']['list']
        if exchange_name == 'binance':
            data = response.json()
        if exchange_name == 'oanda':
            response = response.json()['candles']
            data = []
            for i in response:
                dtt = datetime.datetime.strptime(
                    i['time'][:-4], '%Y-%m-%dT%H:%M:%S.%f')
                time = dtt.strftime('%Y-%m-%d %H:%M')
                data.append({'time': time, 'o': i['mid']['o'], 'h': i['mid']['h'],
                            'l': i['mid']['l'], 'c': i['mid']['c'], 'volume': i['volume']})

        if exchange_name == 'bybit' or 'binance':

            data = [i[:minus] for i in data]
        df = pd.DataFrame(
            data, columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume'])
        df['Time'] = pd.to_datetime(df['Time'], unit='ms', utc=True)
        df['Time'] = df['Time'].dt.strftime('%Y-%m-%d %H:%M')
        if exchange_name == 'bybit':
            df = df.iloc[::-1]
            df = df.reset_index(drop=True)
        return df

    def check_internet_connection(self):
        url = 'https://www.google.com'
        try:
            requests.get(url, timeout=5)
            return True
        except requests.exceptions.RequestException:
            print('Internet connection is not available.')

    def loading_animation(self, text, time_loading: int = 5):
        # Characters to use for animation
        chars = ['⣿', "⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿", '⣿']
        start_time = time.time()  # start time

        while time.time() - start_time < time_loading:  # time condition
            for char in chars:
                # Print the current character
                sys.stdout.write(
                    f'\r {text}  {char} ')
                time.sleep(0.1)  # Wait for a short amount of time
        time.sleep(1)  # Wait for a short amount of time

    def get_bar(self, exchange_name):
        self.ــtimeframe_checkــ()
        arguments = self.symbol, self.timeframe, self.start_time
        # print(exchange_name)
        exchanges = {'bybit': Bybit,
                     'binance': Binance, 'oanda': Oanda}.get(exchange_name)
        if exchanges is None:
            # handle invalid data parameter
            pass
        # print(exchanges)
        exchange = exchanges(*arguments)

        for i in range(self.retry_count):

            # print(retry_count)
            try:
                sys.stdout.write("\033[K")
                self.loading_animation(
                    f'Fetching {self.symbol} new bar for {self.start_time}')
                sys.stdout.write("\033[K")
                sys.stdout.write('\r')
                # sys.stdout.write("\033[K")

                response_data = exchange.bybit_data() if exchange_name == 'bybit' else exchange.binance_data(
                ) if exchange_name == 'binance' else exchange.oanda_data() if exchange_name == 'oanda' else None
                if str(response_data) == '(<Response [200]>, 0)' or '<Response [200]>':
                    # do something with the response
                    break  # if successful, exit the loop
            except requests.exceptions.RequestException:
                # sys.stdout.write("\033[K")
                self.loading_animation(
                    'Request failed: "Encountered network error"  Retrying in 5 seconds')
                sys.stdout.write("\033[K")
                sys.stdout.write('\r')

                if i == self.retry_count - 1:
                    sys.stdout.write("\033[K")
                    sys.exit(
                        '\n Encountered network error: Please check your network')
        sys.stdout.write("\033[K"), sys.stdout.write('\r')
        self.__errors__(exchange_name, response_data)
        bars = self.response_to_json(
            exchange_name, response_data)

        # print(f'Fetching {self.symbol} new bar for {self.start_time}')

        while True:

            last_time = bars['Time'].iloc[-1]
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
                for i in range(self.retry_count):
                    try:

                        sys.stdout.write("\033[K")
                        self.loading_animation(
                            f'Fetching {self.symbol} new bar for {self.start_time}', 2)
                        # sys.stdout.write("\033[K")

                        response_data = exchange.bybit_data() if exchange_name == 'bybit' else exchange.binance_data(
                        ) if exchange_name == 'binance' else exchange.oanda_data() if exchange_name == 'oanda' else None

                        if str(response_data) == '(<Response [200]>, 0)' or '<Response [200]>':
                            sys.stdout.write("\033[K")
                            sys.stdout.write('\r')
                            # sys.exit('hi')
                            # do something with the response
                            break  # if successful, exit the loop

                    except requests.exceptions.RequestException:
                        # sys.stdout.write("\033[K")
                        self.loading_animation(
                            'Request failed: "Encountered network error"  Retrying in 5 seconds')
                        sys.stdout.write("\033[K")
                        sys.stdout.write('\r')

                        if i == self.retry_count - 1:
                            sys.stdout.write("\033[K")
                            sys.exit(
                                '\n Encountered network error: Please check your network')
                self.__errors__(exchange_name, response_data)
                bar2 = self.response_to_json(exchange_name, response_data)
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

    def oanda(self):
        data = self.get_bar('oanda')

        return data


class Oanda(Data):
    def __init__(self,  symbol, time_frame, start_time):
        super().__init__(symbol, time_frame, start_time)

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

        url = f"https://api-fxpractice.oanda.com/v3/instruments/{self.symbol}/candles?price=M&granularity={self.oanda_timeframe()}&from={int(self.date_time_to_timestamp()/1000)}"

        response = requests.get(url, headers=HEADERS)

        return response


# 1675288344
# '2023-03-14 08:00'
print('bars')

data = Data('BTC_USD', '1h', '2023-01-20 11:00')
# 1670601600000
# 1672574400000
# 1636602204
bars = data.oanda()


print(bars)
# TODO oanda {'instrument': 'BTC_USD', 'granularity': 'H1', 'candles': []}
