from s_04.class_test.restaurant import Restaurant

class Flavors:
    def __init__(self, flavors_list=["mango",'haha']):
        self.flavors_list = flavors_list


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        """
        初始化父类的属性。
        再初始化冰激凌小店特有的属性。
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = Flavors()

my_ice = IceCreamStand('xiaowang', 'icecream')

print(my_ice.describe_restaurant())