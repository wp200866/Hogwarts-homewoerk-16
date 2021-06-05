def greet_users(names):

    for name in names:
        msg = f"hello, {name.title()}"
        print(msg)

usernames = ['hannah','try','margot']
greet_users(usernames)