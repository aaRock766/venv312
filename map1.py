class Student:
    name = None

    def say_hi(self):
        print(f"大家好，我是{self.name}，請多多指教")
    def say_hi2(self, msg):
        print(f"大家好，我是{self.name},{msg}")

stu = Student()
stu.say_hi()
stu.name=("周杰倫")
stu.say_hi()

stu2 = Student()
stu2.say_hi()
stu2.name=("林俊傑")
stu2.say_hi()
stu2.say_hi2("我是最因菌的")
