def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


def make_sandwich(*toppings):
    print(f"\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
