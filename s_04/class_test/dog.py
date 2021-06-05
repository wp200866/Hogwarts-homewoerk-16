class Dogs:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        print(f'{self.name} is rolled over')

my_dog = Dogs('huahua', 2)
print(f"my dog name is {my_dog.name}")
print(f"my dog age is {my_dog.age}")
my_dog.sit()
my_dog.roll_over()