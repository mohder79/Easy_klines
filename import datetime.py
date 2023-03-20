import requests
from tqdm import tqdm

url = f'https://api.bybit.com/v5/market/kline?category=inverse&symbol=BTCUSDT&interval=60&start=1670601600000'

with tqdm(total=1, desc="Loading data") as pbar:
    response = requests.get(url)
    pbar.update(1)
