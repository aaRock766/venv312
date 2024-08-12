class Phone:
    __is_5g_enable = True

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5G開啟")
        else:
            print("5g關閉，使用4G")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通話中")

phone = Phone()
phone.call_by_5g()