
import pandas as pd
import datetime


def response_to_json(exchange_name: str, response):
    minus = {'bybit': -1, 'binance': -6}.get(exchange_name)
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
            data.append([time, i['mid']['o'],
                        i['mid']['h'], i['mid']['l'], i['mid']['c'], i['volume']])
        df = pd.DataFrame(
            data, columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume'])

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
