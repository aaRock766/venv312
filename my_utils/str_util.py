def str_reverse(s):
    """
    將傳入的資練反轉
    :param s: 將反轉
    :return: 反轉
    """
    return s[::-1]

def substr(s, x, y):
    """

    :param s:
    :param x:
    :param y:
    :return:
    """
    return s[x:y]

if __name__ == '__main__':
    a = str_reverse("12manhg67")
    print(a)

    b=substr('ddfegrr',2,6)
    print(b)
