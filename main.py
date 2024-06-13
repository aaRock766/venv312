AA = "我今天很快樂 %s" % "小小"
name = "Rock"
stock_price = 20.23
stock_code = "2121"
stock_price_daily_factor = 1.3
growth_days = 3

finally_stock_price = stock_price * stock_price_daily_factor ** growth_days

print(f"公司:{name}, 股票代碼: {stock_code}, 當前股價{stock_price}")
print("每日增長系數： %.1f，經過 %d天後，股價達到： %.2f"% (stock_price_daily_factor,growth_days,finally_stock_price))
print(f"經過{growth_days}天後，股價為{finally_stock_price}")
