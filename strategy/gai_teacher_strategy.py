from ccxt import Exchange
from ccxt.base.types import Ticker

from strategy.base_strategy import BaseStrategy


class GaiTeacherStrategy(BaseStrategy):
    # ===============【2) 交易參數】===============
    rsi_period = 14
    ema_period = 200
    # 順勢加倉參數
    base_buy_pct = 0.15  # 初始買入比例 15%
    increase_step = 0.05  # 每次加倉增加 5%
    times_bought = 0  # 已加倉次數（初始為 0）

    # 設定最大買入數量（例如每次最多買 50）
    max_buy_qty = 30

    def __init__(self, exchange: Exchange):
        super().__init__(exchange)

    def on_init(self, symbol):
        print("on_init")

    def on_tick(self, ticker: Ticker):
        print("on_tick")
        # 請蓋老師實作

    def on_stop(self):
        print("on_stop")
