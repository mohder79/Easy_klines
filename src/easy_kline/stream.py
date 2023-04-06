from .loading_animation    import loading_animation    
from .get_bar import Get_Bar
import pandas as pd
import inspect
import linecache
import re
from .datetime_to_timestamp import date_time_to_timestamp

import pickle
from datetime import timedelta
from .timeframe_converter import timeframe_converter
import os
import sys

def while_loop_checker_and_arg_var_giver():
    # 1. Get the current frame
    current_frame = inspect.currentframe()
    outer_frames = inspect.getouterframes(current_frame)[1:]
    num_lines = sum(frame[2] for frame in outer_frames)

    # 2. Get the previous frame (which should be the frame of the calling function)
    previous_frame = current_frame.f_back

    # 3. Get the line number of the previous frame
    
    for i in range(1 ,num_lines,1):
        previous_lineno = previous_frame.f_lineno - i

    # 4. Get the filename of the previous frame
        previous_filename = previous_frame.f_globals["__file__"]

    # 5. Get the previous line of code
        previous_line = linecache.getline(previous_filename, previous_lineno).strip()
        if 'while' in previous_line:
            sys.stdout.write("\033[K")
            sys.stdout.write('\r')

        if 'easy_klinee.bybit' in previous_line :

            
            arg = re.findall( r"'(.*?)'" , previous_line)
            match = re.search(r'.*(?=\=)', previous_line)
            if match :
                var_name = match.group(0).strip()
            

            break
    return arg 


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Call this function whenever you want to clear the console output


import datetime
def stream():
    '''
    This function starts streaming data based on the symbol and timeframe that you have previously selected.
    
    '''
    
    
    
    
    with open('easy_kline.pickle', 'rb') as f:
        arg = pickle.load(f)
        

    end_time =datetime.datetime.strptime( arg['end_time'][0], '%Y-%m-%d %H:%M')
    timeframe =timeframe_converter(arg['timeframe'][0])

    
    utc_time = datetime.datetime.strptime(  arg['utc_time'][0] , '%Y-%m-%d %H:%M') # utc time in to the pickle file
    utc_time_plus_timeframe =  (
                    utc_time + timedelta(minutes=timeframe)).strftime('%Y-%m-%d %H:%M')
    last_time = date_time_to_timestamp(arg['end_time'][0] )
    # print(end_time)
    new_time = (
            end_time + timedelta(minutes=timeframe)).strftime('%Y-%m-%d %H:%M')
    new2_time = (
            datetime.datetime.strptime( new_time, '%Y-%m-%d %H:%M') + timedelta(minutes=timeframe)).strftime('%Y-%m-%d %H:%M')
    # print(new2_time)
    nn=(end_time + timedelta(minutes=(2 * timeframe))).strftime('%Y-%m-%d %H:%M')
    while True :
        if arg['timeframe'][0] == '1m' :
            candel_closeing_timestamp = date_time_to_timestamp(datetime.datetime.strptime( new_time, '%Y-%m-%d %H:%M').strftime('%Y-%m-%d %H:%M')) 
        else :
            candel_closeing_timestamp = (end_time + timedelta(minutes=(2 * timeframe)-1)).strftime('%Y-%m-%d %H:%M')
            # print(candel_closeing_timestamp)

            candel_closeing_timestamp = date_time_to_timestamp(datetime.datetime.strptime( candel_closeing_timestamp, '%Y-%m-%d %H:%M').strftime('%Y-%m-%d %H:%M')) 
           
        candel_closeing_time = datetime.datetime.strptime( new_time, '%Y-%m-%d %H:%M').strftime('%Y-%m-%d %H:%M')
        loading_animation(f'stop for closing candle {candel_closeing_time} UTC.time is {datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")}',1)

        
        utc_time_now =date_time_to_timestamp(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M'))
        
        

        if utc_time_now > candel_closeing_timestamp :
            # print('oh yes')

            get_bar = Get_Bar(arg['symbol'][0] , arg['timeframe'][0] , new_time ,stream=True , futures = arg['futures'][0])
            new_bars =  get_bar.get_bars(arg['exchange_name'][0])
            # arg['auto_print'][0] =True
            with open('easy_kline.pickle', 'rb') as f:
                arg = pickle.load(f)
            # bars = pd.concat([arg['bars'][0] , new_bars]).reset_index(drop= True)
            bars = pd.DataFrame(arg['bars'][0])
            # print(bars)

                
            break
    return bars
                
                   
