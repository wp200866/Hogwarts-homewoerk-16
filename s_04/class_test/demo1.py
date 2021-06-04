# 创建一个人类
# 通过 class 关键字，定义了一个类
class Person:
    # 类变量
    name = "default"
    age = 0
    gender = 'male'
    weight = 0

    # 构造方法，在类实例化的时候被调用
    def __init__(self,name,age,gender,weight):
        # self.变量名的方式，访问的问题，叫做实例变量
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        print("init function")

    # def set_param(self,name):
    #     self.name = name
    # def set_age(self,age):
    #     self.age = age

    @classmethod
    def eat(self):
        print(f"{self.name} eating")
        print("xxxx")

    def play(self):
        print(f"{self.name} playing")

    def jump(self):
        print(f"{self.name} jump")

# 类方法和实例方法的区别
# 类方法是不能访问 实例方法
# 类方法需要添加一个装饰器 @classmethod

Person.eat()


# 类变量和实例变量的区别，
# 类变量是需要类来访问的，实例变量需要实例来访问

# Person.name = 'tom'
# print(Person.name)
#
# zs = Person('zhangsan',20,'男',130)
# zs.name = 'lili'
# print(zs.name)
# zs.eat()
#
# # zs.set_param('zhangsan')
# # zs.set_age(20)
#
# print(f"zhangsan的名字是：{zs.name}, 年龄是：{zs.age}, 性别是：{zs.gender}, 体重是：{zs.weight}")
#
# ls = Person('lisi',25,'男',150)
# ls.jump()
# print(f"lisi的名字是：{ls.name}, 年龄是：{ls.age}, 性别是：{ls.gender}, 体重是：{ls.weight}")