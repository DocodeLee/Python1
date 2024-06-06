def pizza(size, *toppings):
    print(f"making {size} size pizza")
    for topping in toppings:
        print(f"- {topping}")