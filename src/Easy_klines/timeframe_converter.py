def timeframe_converter(timeframe):
    time = timeframe
    times = {'1m': 1, '3m': 3, '5m': 5, '15m': 15, '30': 30, '1h': 60,
             '2h': 120, '4h': 240, '6h': 360, '8h': 480, '12h': 720, '1d': 1440, '1w': 10080}
    return times.get(time)
