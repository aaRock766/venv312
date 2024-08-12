class Phone:
    IMEI = None
    pro= "HJ"

    def call_by_5G(self):
        print("5G")

class Phone2022(Phone):
    pro ="ddd"

    def call_by_5G(self):
        print("6G")

phone= Phone2022()
phone.call_by_5G()
print(f"父類{Phone.pro}")
# Phone.call_by_5G(self)
print(f"{phone.pro}")


print(f"{super().pro}")