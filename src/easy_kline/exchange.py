
import pandas as pd
from .get_bar import Get_Bar
import linecache
import inspect
import requests
pd.set_option('display.max_rows', None)  # fix *** to show all rows
pd.set_option('display.max_column', None)  # fix *** to show all rows

import re

def binance(symbol : str, time_frame : str, start_time : str,futures : bool =False, retry_count: int = 5 , auto_print : bool =False):

    '''
        
    symbol: The name of the financial symbol for which you want to fetch data.
            Examples include BTCUSDT, SOLUSDT, ETHUSDT , ADAUSDT,...
            To view a complete list of symbols for binance, you can use the binance_symbol() function provided in the easy_klinee module."
    
    time_frame: The time frame at which you want to fetch data.
            Possible values are ['1m', '3m', '5m','15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '1w'].
    
    start_time: The date and time from which you want to start fetching the data. 
            The format should be in YYYY-MM-DD HH:MM.
    
    
    futures : The futures parameter is a boolean value that determines whether the symbol being queried is a futures contract or a spot trading symbol. 
            If futures is set to False (which is the default), the function will fetch data for a spot trading symbol. 
            If futures is set to True, the function will fetch data for a futures trading symbol.
    
    retry_count: The number of times the function will retry fetching data in case of a bad connection.
            The default value is set to 5.

    auto_print: The auto_print parameter in the function is a boolean value that is False by default. 
            If auto_print is set to True, the data will be printed automatically without requiring any additional code to be written for printing.
            When auto_print is set to True, the data will be printed automatically as soon as it is fetched. 
            However, in streaming mode, only the last data point will be printed. 
    '''

    arguments = symbol, time_frame, start_time,futures , retry_count , auto_print
    bar = Get_Bar(*arguments)

    data = bar.get_bars('binance')

    return data

def bybit(symbol : str, time_frame : str, start_time : str,futures : bool =False, retry_count: int = 5 , auto_print : bool =False):
    '''
        
    symbol: The name of the financial symbol for which you want to fetch data.
            Examples include BTCUSDT, SOLUSDT, ETHUSDT , ADAUSDT,...
            To view a complete list of symbols for Bybit, you can use the bybit_symbol() function provided in the easy_klinee module."
    
    time_frame: The time frame at which you want to fetch data.
            Possible values are ['1m', '3m', '5m','15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '1w'].
    
    start_time: The date and time from which you want to start fetching the data. 
            The format should be in YYYY-MM-DD HH:MM.
    
    
    futures : The futures parameter is a boolean value that determines whether the symbol being queried is a futures contract or a spot trading symbol. 
            If futures is set to False (which is the default), the function will fetch data for a spot trading symbol. 
            If futures is set to True, the function will fetch data for a futures trading symbol.
    
    retry_count: The number of times the function will retry fetching data in case of a bad connection.
            The default value is set to 5.

    auto_print: The auto_print parameter in the function is a boolean value that is False by default. 
            If auto_print is set to True, the data will be printed automatically without requiring any additional code to be written for printing.
            When auto_print is set to True, the data will be printed automatically as soon as it is fetched. 
            However, in streaming mode, only the last data point will be printed. 
    '''
          
    frame = inspect.currentframe().f_back
    line_number = frame.f_lineno
    filename = inspect.getframeinfo(frame).filename
    previous_lineno = linecache.getline(filename, line_number).strip()
    match = re.search(r'.*(?=\=)', previous_lineno)
    if match :
        var_name = match.group(0).strip()

        
    arguments = symbol, time_frame, start_time,futures , retry_count  , auto_print
    bar = Get_Bar(*arguments )
    data = bar.get_bars('bybit')

    return data

def oanda(symbol:str, time_frame:str, start_time: str, retry_count: int = 5, auto_print: str =False):
    '''
        
    symbol: The name of the financial symbol for which you want to fetch data.
            Examples include  EUR_CAD, CAD_JPY, GBP_NZD, Gold, Gold_CAD, US_SPX_500.
            To view a complete list of symbols for Oanda, you can use the oanda_symbol() function provided in the easy_klinee module."
            
    
    time_frame: The time frame at which you want to fetch data.
            Possible values are ['1m', '3m', '5m','15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '1w'].
    
    start_time: The date and time from which you want to start fetching the data. 
            The format should be in YYYY-MM-DD HH:MM.
    
    retry_count: The number of times the function will retry fetching data in case of a bad connection.
            The default value is set to 5.

    auto_print: The auto_print parameter in the function is a boolean value that is False by default. 
            If auto_print is set to True, the data will be printed automatically without requiring any additional code to be written for printing.
            When auto_print is set to True, the data will be printed automatically as soon as it is fetched. 
            However, in streaming mode, only the last data point will be printed. 
    '''
    arguments = symbol, time_frame, start_time,False , retry_count  , auto_print
    bar = Get_Bar(*arguments)

    data = bar.get_bars('oanda')

    return data
def oanda_symbol():
    '''
    return oanda symbol list
    '''

    data={1: {'name': 'AU200_AUD', 'displayName': 'Australia', 'type': 'CFD'}, 2: {'name': 'AUD_CAD', 'displayName': 'AUD/CAD', 'type': 'CURRENCY'}, 
3: {'name': 'AUD_CHF', 'displayName': 'AUD/CHF', 'type': 'CURRENCY'}, 4: {'name': 'AUD_HKD', 'displayName': 'AUD/HKD', 'type': 'CURRENCY'}, 
5: {'name': 'AUD_JPY', 'displayName': 'AUD/JPY', 'type': 'CURRENCY'}, 6: {'name': 'AUD_NZD', 'displayName': 'AUD/NZD', 'type': 'CURRENCY'}, 
7: {'name': 'AUD_SGD', 'displayName': 'AUD/SGD', 'type': 'CURRENCY'}, 8: {'name': 'AUD_USD', 'displayName': 'AUD/USD', 'type': 'CURRENCY'}, 
9: {'name': 'BCO_USD', 'displayName': 'Brent', 'type': 'CFD'}, 10: {'name': 'CAD_CHF', 'displayName': 'CAD/CHF', 'type': 'CURRENCY'}, 11: {'name': 'CAD_HKD', 'displayName': 'CAD/HKD', 'type': 'CURRENCY'}, 12: {'name': 'CAD_JPY', 'displayName': 'CAD/JPY', 'type': 'CURRENCY'}, 13: 
{'name': 'CAD_SGD', 'displayName': 'CAD/SGD', 'type': 'CURRENCY'}, 14: {'name': 'CH20_CHF', 'displayName': 'Switzerland', 'type': 'CFD'}, 15: {'name': 'CHF_HKD', 'displayName': 'CHF/HKD', 'type': 'CURRENCY'}, 16: {'name': 'CHF_JPY', 'displayName': 'CHF/JPY', 'type': 'CURRENCY'}, 
17: {'name': 'CHF_ZAR', 'displayName': 'CHF/ZAR', 'type': 'CURRENCY'}, 18: {'name': 'CHINAH_HKD', 'displayName': 'China', 'type': 'CFD'}, 19: {'name': 'CN50_USD', 'displayName': 'China', 'type': 'CFD'}, 20: {'name': 'CORN_USD', 'displayName': 'Corn', 'type': 'CFD'}, 21: {'name': 
'DE10YB_EUR', 'displayName': 'Bund', 'type': 'CFD'}, 22: {'name': 'DE30_EUR', 'displayName': 'Germany', 'type': 'CFD'}, 23: {'name': 'ESPIX_EUR', 'displayName': 'Spain', 'type': 'CFD'}, 24: {'name': 'EU50_EUR', 'displayName': 'Europe', 'type': 'CFD'}, 25: {'name': 'EUR_AUD', 'displayName': 'EUR/AUD', 'type': 'CURRENCY'}, 26: {'name': 'EUR_CAD', 'displayName': 'EUR/CAD', 'type': 'CURRENCY'}, 27: {'name': 'EUR_CHF', 'displayName': 'EUR/CHF', 'type': 'CURRENCY'}, 28: {'name': 'EUR_CZK', 'displayName': 'EUR/CZK', 'type': 'CURRENCY'}, 29: {'name': 'EUR_DKK', 
'displayName': 'EUR/DKK', 'type': 'CURRENCY'}, 30: {'name': 'EUR_GBP', 'displayName': 'EUR/GBP', 'type': 'CURRENCY'}, 31: {'name': 'EUR_HKD', 'displayName': 'EUR/HKD', 'type': 'CURRENCY'}, 32: {'name': 'EUR_HUF', 'displayName': 'EUR/HUF', 'type': 'CURRENCY'}, 33: {'name': 'EUR_JPY', 'displayName': 'EUR/JPY', 'type': 'CURRENCY'}, 34: {'name': 'EUR_NOK', 'displayName': 'EUR/NOK', 'type': 'CURRENCY'}, 35: {'name': 'EUR_NZD', 'displayName': 'EUR/NZD', 'type': 'CURRENCY'}, 36: {'name': 'EUR_PLN', 'displayName': 'EUR/PLN', 'type': 'CURRENCY'}, 37: {'name': 'EUR_SEK', 'displayName': 'EUR/SEK', 'type': 'CURRENCY'}, 38: {'name': 'EUR_SGD', 'displayName': 'EUR/SGD', 'type': 'CURRENCY'}, 39: {'name': 'EUR_TRY', 'displayName': 'EUR/TRY', 'type': 'CURRENCY'}, 40: {'name': 'EUR_USD', 'displayName': 'EUR/USD', 'type': 'CURRENCY'}, 41: {'name': 'EUR_ZAR', 'displayName': 'EUR/ZAR', 'type': 'CURRENCY'}, 42: {'name': 'FR40_EUR', 'displayName': 'France', 'type': 'CFD'}, 43: {'name': 'GBP_AUD', 'displayName': 'GBP/AUD', 'type': 'CURRENCY'}, 44: {'name': 'GBP_CAD', 'displayName': 'GBP/CAD', 'type': 'CURRENCY'}, 45: {'name': 
'GBP_CHF', 'displayName': 'GBP/CHF', 'type': 'CURRENCY'}, 46: {'name': 'GBP_HKD', 'displayName': 'GBP/HKD', 'type': 'CURRENCY'}, 47: {'name': 'GBP_JPY', 'displayName': 'GBP/JPY', 'type': 'CURRENCY'}, 48: {'name': 'GBP_NZD', 'displayName': 'GBP/NZD', 'type': 'CURRENCY'}, 49: {'name': 'GBP_PLN', 'displayName': 'GBP/PLN', 'type': 'CURRENCY'}, 50: {'name': 'GBP_SGD', 'displayName': 'GBP/SGD', 'type': 'CURRENCY'}, 51: {'name': 'GBP_USD', 'displayName': 'GBP/USD', 'type': 'CURRENCY'}, 52: {'name': 'GBP_ZAR', 'displayName': 'GBP/ZAR', 'type': 'CURRENCY'}, 53: {'name': 'HK33_HKD', 'displayName': 'Hong', 'type': 'CFD'}, 54: {'name': 'HKD_JPY', 'displayName': 'HKD/JPY', 'type': 'CURRENCY'}, 55: {'name': 'JP225_USD', 'displayName': 'Japan', 'type': 'CFD'}, 56: {'name': 'JP225Y_JPY', 'displayName': 'Japan', 'type': 'CFD'}, 57: {'name': 'NAS100_USD', 'displayName': 'US', 'type': 'CFD'}, 58: {'name': 'NATGAS_USD', 'displayName': 'Natural', 'type': 'CFD'}, 59: {'name': 'NL25_EUR', 'displayName': 'Netherlands', 'type': 'CFD'}, 60: {'name': 'NZD_CAD', 'displayName': 'NZD/CAD', 'type': 'CURRENCY'}, 61: {'name': 'NZD_CHF', 'displayName': 'NZD/CHF', 'type': 'CURRENCY'}, 62: {'name': 'NZD_HKD', 'displayName': 'NZD/HKD', 'type': 'CURRENCY'}, 63: {'name': 'NZD_JPY', 'displayName': 'NZD/JPY', 'type': 'CURRENCY'}, 64: {'name': 'NZD_SGD', 'displayName': 'NZD/SGD', 'type': 'CURRENCY'}, 65: {'name': 'NZD_USD', 'displayName': 'NZD/USD', 'type': 'CURRENCY'}, 66: {'name': 'SG30_SGD', 'displayName': 'Singapore', 'type': 'CFD'}, 67: {'name': 'SGD_CHF', 'displayName': 'SGD/CHF', 'type': 'CURRENCY'}, 68: {'name': 'SGD_JPY', 'displayName': 'SGD/JPY', 'type': 'CURRENCY'}, 69: {'name': 'SOYBN_USD', 'displayName': 'Soybeans', 'type': 'CFD'}, 70: {'name': 'SPX500_USD', 'displayName': 'US', 'type': 'CFD'}, 71: {'name': 'SUGAR_USD', 'displayName': 'Sugar', 'type': 'CFD'}, 72: {'name': 'TRY_JPY', 'displayName': 'TRY/JPY', 'type': 'CURRENCY'}, 73: {'name': 'TWIX_USD', 'displayName': 'Taiwan', 'type': 'CFD'}, 74: {'name': 'UK100_GBP', 'displayName': 'UK', 'type': 'CFD'}, 75: {'name': 'UK10YB_GBP', 'displayName': 'UK', 'type': 'CFD'}, 76: {'name': 'US2000_USD', 'displayName': 'US', 'type': 'CFD'}, 77: {'name': 'US30_USD', 'displayName': 'US', 'type': 'CFD'}, 78: {'name': 'USB02Y_USD', 'displayName': 'US', 'type': 'CFD'}, 79: {'name': 'USB05Y_USD', 'displayName': 'US', 'type': 'CFD'}, 80: {'name': 'USB10Y_USD', 'displayName': 'US', 'type': 'CFD'}, 81: {'name': 'USB30Y_USD', 'displayName': 'US', 'type': 'CFD'}, 82: {'name': 'USD_CAD', 'displayName': 'USD/CAD', 'type': 'CURRENCY'}, 83: {'name': 'USD_CHF', 'displayName': 'USD/CHF', 'type': 'CURRENCY'}, 84: {'name': 'USD_CNH', 'displayName': 'USD/CNH', 'type': 'CURRENCY'}, 85: {'name': 'USD_CZK', 'displayName': 'USD/CZK', 'type': 'CURRENCY'}, 86: {'name': 'USD_DKK', 'displayName': 'USD/DKK', 'type': 'CURRENCY'}, 87: {'name': 'USD_HKD', 'displayName': 'USD/HKD', 'type': 'CURRENCY'}, 88: {'name': 'USD_HUF', 'displayName': 'USD/HUF', 'type': 'CURRENCY'}, 89: {'name': 'USD_JPY', 'displayName': 'USD/JPY', 'type': 'CURRENCY'}, 90: {'name': 'USD_MXN', 'displayName': 'USD/MXN', 'type': 'CURRENCY'}, 91: {'name': 'USD_NOK', 'displayName': 'USD/NOK', 'type': 'CURRENCY'}, 92: {'name': 'USD_PLN', 'displayName': 'USD/PLN', 'type': 'CURRENCY'}, 93: {'name': 'USD_SEK', 'displayName': 'USD/SEK', 'type': 'CURRENCY'}, 94: {'name': 'USD_SGD', 'displayName': 'USD/SGD', 'type': 'CURRENCY'}, 95: {'name': 'USD_THB', 'displayName': 'USD/THB', 'type': 'CURRENCY'}, 96: {'name': 'USD_TRY', 'displayName': 'USD/TRY', 'type': 'CURRENCY'}, 97: {'name': 'USD_ZAR', 'displayName': 'USD/ZAR', 'type': 'CURRENCY'}, 98: {'name': 'WHEAT_USD', 'displayName': 'Wheat', 'type': 'CFD'}, 99: {'name': 'WTICO_USD', 'displayName': 'West', 'type': 'CFD'}, 100: {'name': 'XAG_AUD', 'displayName': 'Silver/AUD', 'type': 'METAL'}, 101: {'name': 'XAG_CAD', 'displayName': 'Silver/CAD', 'type': 'METAL'}, 
102: {'name': 'XAG_CHF', 'displayName': 'Silver/CHF', 'type': 'METAL'}, 103: {'name': 'XAG_EUR', 'displayName': 'Silver/EUR', 'type': 'METAL'}, 104: {'name': 'XAG_GBP', 'displayName': 'Silver/GBP', 'type': 'METAL'}, 105: {'name': 'XAG_HKD', 'displayName': 'Silver/HKD', 'type': 'METAL'}, 106: {'name': 'XAG_JPY', 'displayName': 'Silver/JPY', 'type': 'METAL'}, 107: {'name': 'XAG_NZD', 'displayName': 'Silver/NZD', 'type': 'METAL'}, 108: {'name': 'XAG_SGD', 'displayName': 'Silver/SGD', 'type': 'METAL'}, 109: {'name': 'XAG_USD', 'displayName': 'Silver', 'type': 'METAL'}, 110: {'name': 'XAU_AUD', 'displayName': 'Gold/AUD', 'type': 'METAL'}, 111: {'name': 'XAU_CAD', 'displayName': 'Gold/CAD', 'type': 'METAL'}, 112: {'name': 'XAU_CHF', 'displayName': 'Gold/CHF', 'type': 'METAL'}, 113: {'name': 'XAU_EUR', 'displayName': 'Gold/EUR', 'type': 'METAL'}, 114: {'name': 'XAU_GBP', 'displayName': 'Gold/GBP', 'type': 'METAL'}, 115: {'name': 'XAU_HKD', 'displayName': 'Gold/HKD', 'type': 'METAL'}, 116: {'name': 'XAU_JPY', 'displayName': 'Gold/JPY', 'type': 'METAL'}, 117: {'name': 'XAU_NZD', 'displayName': 'Gold/NZD', 'type': 'METAL'}, 118: {'name': 'XAU_SGD', 'displayName': 'Gold/SGD', 'type': 'METAL'}, 119: {'name': 'XAU_USD', 'displayName': 'Gold', 'type': 'METAL'}, 120: {'name': 'XAU_XAG', 'displayName': 'Gold/Silver', 'type': 'METAL'}, 121: {'name': 'XCU_USD', 'displayName': 'Copper', 'type': 'CFD'}, 122: {'name': 'XPD_USD', 'displayName': 'Palladium', 'type': 'CFD'}, 123: {'name': 'XPT_USD', 'displayName': 'Platinum', 'type': 'CFD'}, 124: {'name': 'ZAR_JPY', 'displayName': 'ZAR/JPY', 'type': 'CURRENCY'}}
    
    symbol = pd.DataFrame.from_dict(data, orient='index')
    return symbol
import requests
import pandas as pd
def bybit_symbol(futures : bool = False):
        '''
        return bybit symbol list
        '''     
       
        if futures :
                futures = 'linear'
        else : 
                futures = 'spot'
        url = f'https://api.bybit.com/v5/market/instruments-info?category={futures}&limit=1000'
        
        
        response = requests.get(url)
        data = response.json()['result']['list']
        

        df = pd.DataFrame(data)
        
        
        
        return df[['symbol' , 'baseCoin', 'quoteCoin' ,'status']]

def binance_symbol(futures : bool = False):
        '''
        return binance symbol list
        '''  
        if futures :
                url = 'https://fapi.binance.com/fapi/v1/exchangeInfo' 
        else : 
                url = 'https://api.binance.com/api/v3/exchangeInfo'
   
        
        
        


        # Make a request to the Binance API to get the exchange information
        response = requests.get(url)

        # Parse the JSON response
        js = response.json()['symbols']
        data = []
        for i in js:
                if i['quoteAsset'] == 'USDT' and futures:
                        x =  {'symbol' :i['symbol'],'quoteAsset' : i['quoteAsset'] , 'baseAsset': i['baseAsset'] , 'contractType' : i['contractType'] , 'status': i['status']}
                        data.append(x)
                elif i['quoteAsset'] == 'USDT' and not futures:
                        x =  {'symbol' :i['symbol']  , 'status': i['status'] ,'quoteAsset' : i['quoteAsset'] , 'baseAsset': i['baseAsset']}
                        data.append(x)

                
        # print(data)
        # symbols = [symbol['symbol'] for symbol in data['symbols']]
        df = pd.DataFrame(data)

        # # Extract the symbols from the exchange_info dictionary

        # # Print the symbols
        return df