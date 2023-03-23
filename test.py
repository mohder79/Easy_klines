from Easy_klines import Easy_klines

data = Easy_klines('BTCUSDT', '1h', '2023-01-20 11:00')

bars = data.bybit()


print(bars)
