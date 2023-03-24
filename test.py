import easy_kline

kline = easy_kline.exchange('BTCUSDT', '1h', '2023-01-20 12:00')
BTCUSDT = kline.binance()


def SMA(data: str, length: int, column: str):
    return data[column].rolling(window=length).mean()


BTCUSDT['sma'] = SMA(BTCUSDT, 14, 'Close')

print(BTCUSDT)
