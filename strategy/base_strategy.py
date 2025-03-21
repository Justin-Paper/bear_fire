from ccxt import Exchange
from ccxt.base.types import Ticker


class BaseStrategy:
    def __init__(self, exchange: Exchange):
        self.symbol = None
        self.exchange = exchange

    def init(self, symbol):
        self.symbol = symbol
        self.on_init(symbol)

    # 請實作
    # 策略開始前的初始
    def on_init(self, symbol):
        pass

    # 請實作
    # 市場價格變化時會呼叫
    def on_tick(self, ticker: Ticker):
        pass  # 實作

    # 請實作
    # 結束時會呼叫
    def on_stop(self):
        pass  # 實作
