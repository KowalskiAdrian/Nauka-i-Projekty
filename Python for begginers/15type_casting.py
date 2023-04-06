age = input("What is yoyr age?")
data_type = type(age)

age = int(age)
data_type = type(age)
print(data_type)

print("Your age in dog years is", (age * 7))


grocery_list = ['Apples', 'Oranges', 'Bananas', 'Apples']
grocery_list = set(grocery_list)
print(grocery_list)
print(type(grocery_list))


grocery_list = ('Ananas', 'Lemon', 'Coconut')
for grocery in grocery_list:
    print("You need to buy", grocery)
    print(type(grocery_list))