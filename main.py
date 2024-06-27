n = 200

def a():
    n=50
    print(n)

def b():
    global n
    n=100
    print(n)

a()
b()
print(n)