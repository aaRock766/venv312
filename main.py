import random
balance = 10000
emploee = 20

while balance > 0:
    for i in range(1,21):
        print(f"第{i}員工")
        perfor = random.randint(1,10)
        print(f"績效:{perfor}")
        if perfor <5:
            print("績效不好，沒有薪水")
            continue
        elif balance<=0:
            print("沒錢了")
            break
        else:
            print("發放1000元")
            balance = balance-400
        print(f"剩餘{balance}")