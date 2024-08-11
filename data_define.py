"""
數據定義的類
"""

class Record:

    def __init__(self, date, order_id, money, province):
        self.date = date            #訂單日期
        self.order_id = order_id    #訂單編號
        self.money = money          #訂單金額
        self.province = province    #省分