from s_04.class_test.user1 import User

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for i in self.privileges:
            print(f"用户  {i}")

class Admin(User):

    def __init__(self, first_name, last_name, age, weight):
        """
        初始化父类的属性。
        再初始化管理员的特有属性。
        """
        super().__init__(first_name, last_name, age, weight)
        self.privileges = Privileges



my_admin = Admin("li","li", 15, 80)
my_admin.privileges.show_privileges()