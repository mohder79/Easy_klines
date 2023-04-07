'''
After successfully obtaining the response data, convert data to a Pandas dataframe and enters a loop that checks if the last retrieved bar is recent.
If it is,breaks out of the loop and returns the bars.
If the last retrieved bar is not recent enough, the method computes the time of the next bar and retrieves it from the exchange using the same process as before.
The retrieved bars are concatenated with the existing dataframe until the last bar retrieved is recent enough.
'''
import pickle
from .datetime_to_timestamp import date_time_to_timestamp

from datetime import timedelta
import pandas as pd
import requests
import datetime
import sys
from .bybit import Bybit
from .binance import Binance
from .oanda import Oanda
from .timeframe_check import timeframe_check
from .errors import errors
from .timeframe_converter import timeframe_converter
from .response_to_json import response_to_json
from .loading_animation import loading_animation
import os
import inspect

class Get_Bar:
    def __init__(self,  symbol, time_frame, start_time,futures =False , retry_count: int = 5  ,auto_print=False , stream=False):
        # print(stream)
        self.symbol = symbol
        self.timeframe = time_frame
        self.start_time = start_time
        self.retry_count = retry_count
        self.futures = futures
        self.stream = stream
        self.auto_print = auto_print
        
        

    def get_bars(self, exchange_name):

        timeframe_check(self.timeframe)
        if exchange_name  in ['bybit' , 'binance'] :
            if self.futures not in [True, False]:
                sys.exit("Wrong category ERROR. It should be True for futures and False for spot. The default is False (spot).")
            arguments = self.symbol, self.timeframe, self.start_time , self.futures
        else :
            arguments = self.symbol, self.timeframe, self.start_time 

        exchanges = {'bybit': Bybit,
                     'binance': Binance, 'oanda': Oanda}.get(exchange_name)
        if exchanges is None:
            pass

        exchange = exchanges(*arguments)

        for i in range(self.retry_count):


            try:
                sys.stdout.write("\033[K")
                loading_animation(
                    f'Fetching a new bar of data for {self.symbol} at {self.start_time}')
                sys.stdout.write("\033[K")
                sys.stdout.write('\r')

                response_data = exchange.bybit_data() if exchange_name == 'bybit' else exchange.binance_data(
                ) if exchange_name == 'binance' else exchange.oanda_data() if exchange_name == 'oanda' else None
                if str(response_data) == '(<Response [200]>, 0)' or '<Response [200]>':
                    break  # if successful, exit the loop
            except requests.exceptions.RequestException:
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

        while True:
            

            last_time = bars['Time'].iloc[-1]
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

                if exchange_name  in ['bybit' , 'binance'] :
                    arguments = self.symbol, self.timeframe, self.start_time , self.futures
                else :
                    arguments = self.symbol, self.timeframe, self.start_time 
                exchange = exchanges(*arguments)
                for i in range(self.retry_count):
                    try:

                        sys.stdout.write("\033[K")
                        loading_animation(
                            f'Fetching {self.symbol} new bar for {self.start_time}', 2)

                        response_data = exchange.bybit_data() if exchange_name == 'bybit' else exchange.binance_data(
                        ) if exchange_name == 'binance' else exchange.oanda_data() if exchange_name == 'oanda' else None

                        if str(response_data) == '(<Response [200]>, 0)' or '<Response [200]>':
                            sys.stdout.write("\033[K")
                            sys.stdout.write('\r')

                            break  # if successful, exit the loop

                    except requests.exceptions.RequestException:
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

        bars.drop(bars.index[-1], inplace=True)
        if  not self.stream :
            try :
                sys.stdout.write("\033[K")
                sys.stdout.write('\r')
                file_name = f'{self.symbol}-{exchange_name}-{self.timeframe}-{self.start_time.replace(":" , "-")}.xlsx'
                excel = pd.ExcelWriter(file_name, engine = 'xlsxwriter')
                bars.to_excel(excel, sheet_name = 'data sheet')

                excel.close()
            except PermissionError :
                sys.exit('\n PermissionError: Permission denied for removig old data plese close the excel file')
            with open('easy_kline.pickle', 'wb') as f:
                utc_time =datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M')
                arg = {'exchange_name' : [exchange_name],'symbol' : [self.symbol] ,'timeframe' : [self.timeframe] , 'start_time' : [self.start_time] , 'end_time' : [bars['Time'].iloc[-1]] , 'utc_time': [utc_time]  , 'bars': [bars] , 'file_name' :[file_name] ,'auto_print' :[self.auto_print] , 'futures': [self.futures]}
                pickle.dump(arg, f)
            if self.auto_print :

                print(bars.to_string())
            
        if self.stream :            
            sys.stdout.write("\033[K")
            sys.stdout.write('\r')
            
            with open('easy_kline.pickle', 'rb') as f:
                arg = pickle.load(f)
                bars3 = arg['bars'][0]
                bars = pd.concat([bars3 , bars]).reset_index(drop=True)
                arg['bars'][0] = bars
                arg['end_time'][0] = bars['Time'].iloc[-1]
                
            with open('easy_kline.pickle', 'wb') as f:
                pickle.dump(arg, f)

                
            if arg['auto_print'][0] :
                
                print(bars.tail(1).to_string(header=False))


        return bars

