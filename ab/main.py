money = 50000000
name = input("請輸入姓名:")

def query(show_header):
    if show_header:
        print("------查詢餘額-----")
    print(f"{name},你的餘額剩餘：{money}元")

def saving(num):
    global money
    money += num
    print("------存款-----")
    print(f"{name},你的存款：{num}元成功")
    query(False)

def get_money(num):
    global  money
    money -=num
    print("------取款-----")
    print(f"{name},你的取款：{num}元成功")
    query(False)

def main():
        print("------主菜單-----")
        print(f"{name}你好，歡迎來到黑馬銀行")
        print("餘額查詢\t【輸入1】")
        print("存款\t\t【輸入2】")
        print("取款\t\t【輸入3】")
        print("退出\t\t【輸入4】")
        return input("請輸入你的選擇:")

while True:
    keyin = main()
    if keyin =="1":
        query()
        continue
    elif keyin =="2":
        num = int(input("你想要存多少錢:"))
        saving(num)
    elif keyin == "3":
        num = int(input("你想要提多少錢:"))
        get_money(num)
    else:
        print("退出循環")
        break