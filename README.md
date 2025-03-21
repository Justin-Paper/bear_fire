# 🐻 大群被動收入永動系統

## 前言
此系統為 🐻 大群專屬，未來展望就是可透過此系統賺點本金投入土狗，土狗失去的再從這邊要回來。

## 如何安裝
* 下載此專案或透過 git clone下載
* 需安裝python環境
* 使用命令字元於專案根目錄執行：
```shell
pip install -r requirements.txt
```

## 如何設定
* 將根目錄的**accounts_sample.json** 改名為 **accounts.json**，並開啟檔案設定交易所的api_key等資訊


## 如何開始寫策略(蓋老師的天下)
* 根目錄下有strategy資料夾，下方有個gai_teacher_strategy.py檔案，這裡只能請蓋老師完成它
* 實作說明：
```python
    # 開始跑策略前會先執行此函數，可以設定一些前置作業例如指標的參數等
    def on_init(self, symbol):
        print("on_init")

    # 價格變動會呼叫此函數，ticker為目前最新的資訊，如價格等
    def on_tick(self, ticker: Ticker):
        # 這邊要請蓋老師實作

     # 策略執行結束時呼叫
    def on_stop(self):
        print("on_stop")
```

## 未完成目標 Feature 
* 蓋老師的策略
* 可執行回歸測試功能
* 可請群友提議