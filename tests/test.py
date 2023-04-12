import easy_klinee
import pandas as pd

# Hello to everybody
def SMA(data: str, length: int, column: str):
    return data[column].rolling(window=length).mean()

kline = easy_klinee.bybit('BTCUSDT', '1m', '2023-04-6 14:01',auto_print = False )
while True :
    kline = easy_klinee.stream()    
    
    kline['sma'] = SMA(kline , 14 , 'Close')
    print(kline)

print("Welcome to Bitcoin")


