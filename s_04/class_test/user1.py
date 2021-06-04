class User:
    def __init__(self, first_name, last_name, age, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.weight = weight
        self.login_attempts = 0

    def describe_user(self):
        print(f"describe : fist_name is {self.first_name},last_name is {self.last_name},age is {self.age},weight is {self.weight}")

    def greet_user(self):
        print(f"hello {self.first_name}{self.last_name},welcome!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# zs = User("zhang","san",15,150)
# zs.describe_user()
# zs.greet_user()
# zs.greet_user()

# zs.increment_login_attempts()
# zs.increment_login_attempts()
# zs.increment_login_attempts()
# print(zs.login_attempts)
#
# zs.reset_login_attempts()
# print(zs.login_attempts)