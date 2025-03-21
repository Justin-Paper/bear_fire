import ccxt
import time
from datetime import datetime, timezone

from strategy.gai_teacher_strategy import GaiTeacherStrategy
from utils import get_account_configs

# =============== 初始設定 ===============
exchange_name = input("請輸入你要使用的交易所\n ex. binance, okx, bitget, mexc...：")
configs = get_account_configs()
if exchange_name not in configs or len(configs[exchange_name]['api_key']) == 0:
    print(f"⚠️請確認{exchange_name}是否有在account.json設定api key相關參數")
    exit()
if exchange_name not in ccxt.exchanges:
    print(f"⚠️目前{exchange_name}交易所不支援")
    exit()

symbol = input("請輸入要執行的交易對\n ex BTC/USDT, ETH/USDT, SOL/USDT...：")

is_test: int = 0
while True:
    is_test = int(input("是否為模擬倉 (0:不是, 1:是)："))
    if is_test != 0 and is_test != 1:
        print("⚠️請輸入0或1")
    else:
        break


api_key = configs[exchange_name]['api_key']
api_secret = configs[exchange_name]['secret']
passphrase = "" if 'password' not in configs[exchange_name] else configs[exchange_name]['password']


exchange_obj = getattr(ccxt, exchange_name)
# 連接交易所
exchange = exchange_obj({
    "apiKey": api_key,
    "secret": api_secret,
    "password": passphrase,
    "enableRateLimit": True,
    "options": {"defaultType": "spot"},
})

exchange.set_sandbox_mode(True if is_test else False)
market = exchange.load_markets()
print(market)

# 用來記錄程式啟動時間
start_time = datetime.now(timezone.utc)

strategy = GaiTeacherStrategy(exchange)

try:
    strategy.init(symbol)
    update_duration_range = range(8, 12)

    while True:
        dateTimeStr = datetime.now().isoformat(timespec="milliseconds")
        print(f"\n🔄 更新市場數據..... 更新時間: {dateTimeStr}")

        ticker = exchange.fetch_ticker(symbol)
        print(f"{symbol} 目前價格: {ticker['last']}")

        strategy.on_tick(ticker)
        ticked_time = datetime.now()
        next_sleep = update_duration_range.stop
        if ticked_time.second >= 45:
            next_sleep = 60 - ticked_time.second + 1
        elif ticked_time.second < 25:
            next_sleep = update_duration_range.stop
        else:
            next_sleep = update_duration_range.start

        time.sleep(next_sleep)
except KeyboardInterrupt:
    print("程式已結束。")
