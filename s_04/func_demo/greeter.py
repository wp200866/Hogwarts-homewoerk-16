# def get_formatted_name(first_name, last_name):
#     """返回整洁的姓名。"""
#     full_name = f'{first_name} {last_name}'
#     return full_name.title()
#
# # 这是一个无限循环！
# while True:
#     print("\nPlease tell me your name")
#     print("(enter 'q' at any time to quit)")
#
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#
#     formatted_name = get_formatted_name(f_name,l_name)
#     print(f"\nHello, {formatted_name}")

# def city_country(city_name,county_name):
#     full_city = f'"{city_name}, {county_name}"'
#     return full_city.title()
#
# new_city = city_country("shenzhen","guangdong")
# print(new_city)

def make_album(singer,album):
    full_album = {"singer":singer,"album":album}
    return full_album

album1 = make_album('liudehua', 'tiantian')
print(album1)
