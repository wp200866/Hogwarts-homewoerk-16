class Car:
    def __init__(self, make, model, year):
        '''初始化描述汽车的属性。'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 100

    def get_descriptive_name(self):
        """返回整洁的描述性信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条支出汽车里程的消息。"""
        print(f"This car is has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读书设置为指定的值。
        禁止将里程表读数往回调。
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量。"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

# my_new_car = Car("audi", "a4", 2019)
# print(my_new_car.get_descriptive_name())

# # 1、直接修改属性值
# my_new_car.odometer_reading = 23

# # 2、通过方法修改属性的值
# my_new_car.update_odometer(23)

# 3、通过方法对属性的值进行递增
# my_new_car.update_odometer(23_500)
# my_new_car.read_odometer()
#
# my_new_car.increment_odometer(-100)
# my_new_car.read_odometer()
