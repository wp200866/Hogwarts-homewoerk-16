class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"This restaurant name is {self.restaurant_name}, 最好吃的是{self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is opening")

    def number_serving(self, number):
        self.number_served = number

    def set_number_served(self, may_number):
        self.number_served = may_number

# my_restaurant = Restaurant("xiangcai","midoufu")
# print(f"餐厅的名字是{my_restaurant.restaurant_name},特色菜是{my_restaurant.cuisine_type}")
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

# print(f"开业后的就餐人数为{my_restaurant.number_servered}")
# my_restaurant.number_servered = 58

# my_restaurant.number_serving(22)
#
# print(f"开业后的就餐人数为{my_restaurant.number_served}")
#
# my_restaurant.set_number_served(100)
# print(f"每天可能的就餐人数为{my_restaurant.number_served}")

