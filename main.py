import MetaTrader5 as mt5

mt5.initialize()

account = 1234567
selected = mt5.select_account(account)

balance = mt5.account_info().balance

symbol = "EURUSD"
lot = 0.01

result = mt5.order_send(symbol=symbol, action=mt5.ORDER_TYPE_BUY, volume=lot, price=mt5.symbol_info_tick(symbol).ask, deviation=20)

mt5.shutdown()
