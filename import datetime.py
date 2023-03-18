import requests
from datetime import datetime
import time
# تنظیم پارامترهای مورد نیاز
symbol = "BTCUSDT"  # نماد معاملاتی
interval = '1hour'  # بازه زمانی
start_date = "2022-01-01"  # تاریخ شروع
end_date = "2022-01-02"  # تاریخ پایان

# محاسبه timestamp مربوط به تاریخ شروع
start_timestamp = int(datetime.timestamp(datetime.fromisoformat(start_date)))
# محاسبه timestamp مربوط به تاریخ پایان
end_timestamp = int(datetime.timestamp(datetime.fromisoformat(end_date)))
start_time = 1609459200000  # تاریخ شروع در میلی ثانیه
end_time = int(time.time() * 1000)
# ارسال درخواست به API
url = f"https://api.coinex.com/v1/market/kline?market={symbol}&type={interval}&end_time={end_time}"
response = requests.get(url)
data = response.json()
print(data)
