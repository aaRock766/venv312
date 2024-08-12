class AC:
    def cool_wind(self):
        pass

    def hot_wind(self):
        pass

    def swing_l_r(self):
        pass
class Midea_AC(AC):
    def cool_wind(self):
        print("美地製冷")
    def hot_wind(self):
        print("美地炙熱")
    def swing_l_r(self):
        print("美地左右百封")


class Green_AC(AC):
    def cool_wind(self):
        print("蛤蠣製冷")

    def hot_wind(self):
        print("蛤蠣炙熱")

    def swing_l_r(self):
        print("蛤蠣百封")


def make_cool(ac :AC):
    ac.cool_wind()

midea_ac=Midea_AC()
green_ac=Green_AC()

make_cool(midea_ac)
