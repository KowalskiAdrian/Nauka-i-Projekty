# def person(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
    
#     if 'age' in kwargs:
#         print("Your age is", kwargs.get("age"))

# person(name="Adrian", age=33, brain="huge")


def order_pizza(name, address, pizzaname, **toppings):
    print(f"Order is for {name}")
    print(f"Ship it to {address}")
    print(f"You chose pizza {pizzaname}")            
    price = 18.00
    for key, value in toppings.items():
        price = price + 2.00 
    print(f"The total price is {price}")
    return price

total_price = order_pizza("Adrian", "Poland", "Americana", pepperoni=True, extra_cheese=True, salami=True, olives=True)