class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"student對象, name:{self.name}, age:{self.age}"

    # def __lt__(self, other):
    #     return self.age < other.age


stu1 = Student("周杰倫", 31)
stu2= Student("林苦五", 21)
print(stu1<stu2)
