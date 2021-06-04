def make_car(factory,size,**user_info):
    user_info['factory'] = factory
    user_info['size'] = size
    return user_info

car = make_car('sabaru', 'omutback', color='blue', tow_package=True)
print(car)