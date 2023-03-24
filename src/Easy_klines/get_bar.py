
from datetime import timedelta
import pandas as pd
import requests
import datetime
import sys
from bybit import Bybit
from binance import Binance
from oanda import Oanda
from datetime_to_timestamp import date_time_to_timestamp
from timeframe_check import timeframe_check
from errors import *
from timeframe_converter import *
from response_to_json import *
from loading_animation import *


class Get_Bar:
    def __init__(self,  symbol, time_frame, start_time, retry_count: int = 5):

        self.symbol = symbol
        self.timeframe = time_frame
        self.start_time = start_time
        self.retry_count = retry_count

    def get_bar(self, exchange_name):
        timeframe_check(self.timeframe)
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
                loading_animation(
                    f'Fetching {self.symbol} new bar for {self.start_time}')
                sys.stdout.write("\033[K")
                sys.stdout.write('\r')
                # sys.stdout.write("\033[K")

                response_data = exchange.bybit_data() if exchange_name == 'bybit' else exchange.binance_data(
                ) if exchange_name == 'binance' else exchange.oanda_data() if exchange_name == 'oanda' else None
                # print(response_data)
                if str(response_data) == '(<Response [200]>, 0)' or '<Response [200]>':
                    # do something with the response
                    break  # if successful, exit the loop
            except requests.exceptions.RequestException:
                # sys.stdout.write("\033[K")
                loading_animation(
                    'Request failed: "Encountered network error"  Retrying in 5 seconds')
                sys.stdout.write("\033[K")
                sys.stdout.write('\r')

                if i == self.retry_count - 1:
                    sys.stdout.write("\033[K")
                    sys.exit(
                        '\n Encountered network error: Please check your network')
        sys.stdout.write("\033[K"), sys.stdout.write('\r')
        errors(exchange_name, response_data)
        bars = response_to_json(
            exchange_name, response_data)
        # print(bars)
        # print(f'Fetching {self.symbol} new bar for {self.start_time}')

        while True:

            last_time = bars['Time'].iloc[-1]
            # for test
            # last_row_mask = bars.index == (len(bars) - 1)
            # bars.loc[last_row_mask,
            #          'volume'] = 'XXXXXXXXSSSSAAAAAZZZZZZXXXXX'
            #
            time_now = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M')
            time = timeframe_converter(self.timeframe)
            time_format = "%Y-%m-%d %H:%M"
            time1 = datetime.datetime.strptime(time_now, time_format)
            time2 = datetime.datetime.strptime(
                str(last_time), str(time_format))

            difference_in_minutes = (time1 - time2).total_seconds() // 60
            if difference_in_minutes <= time:
                break
            else:

                last_bar_datetime = datetime.datetime.strptime(
                    last_time, '%Y-%m-%d %H:%M')
                new_time = (
                    last_bar_datetime + timedelta(minutes=time)).strftime('%Y-%m-%d %H:%M')
                if new_time == self.start_time:

                    break

                self.start_time = new_time

                arguments = self.symbol, self.timeframe, self.start_time
                exchange = exchanges(*arguments)
                for i in range(self.retry_count):
                    try:

                        sys.stdout.write("\033[K")
                        loading_animation(
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
                        loading_animation(
                            'Request failed: "Encountered network error"  Retrying in 5 seconds')
                        sys.stdout.write("\033[K")
                        sys.stdout.write('\r')

                        if i == self.retry_count - 1:
                            sys.stdout.write("\033[K")
                            sys.exit(
                                '\n Encountered network error: Please check your network')
                errors(exchange_name, response_data)
                bar2 = response_to_json(exchange_name, response_data)
                bars = pd.concat([bars, bar2]).reset_index(drop=True)
                # last_row_mask = bars.index == (len(bars) - 1)
                # bars.loc[last_row_mask,
                #          'volume'] = 'XXXXXXXXXXXXX'
        bars.drop(bars.index[-1], inplace=True)

        return bars
