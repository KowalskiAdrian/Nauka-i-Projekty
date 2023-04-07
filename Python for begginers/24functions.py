# def somename(name, food="Pizza"):
#     print(f"Hello {name}. Let eat some {food}")
    
# somename('Adrian')

# def somename(name, food="Pizza"):
#     print(f"Hello {name}. Let eat some {food}")
    
# somename('Adrian', 'Bannana')

# def somename(name, food="Pizza"):
#     if name.lower() == "peter":
#         print("Welcome Peter")
        
#     print(f"Hello {name}. Let eat some {food}")
    
# somename('Peter', food='Bannana')

# def somename(name=None, food="Pizza"):
#     if name is None:
#         name = "Kleofas"
        
#     person_type = "human"
#     if name == "Kleofas":
#         person_type = "Cat" 
        
#     print(person_type)
        
#     print(f"Hello {name}. Let eat some {food}")
    
# some_var = somename()

# print("The variable is ", some_var)

# def somefunction():
#     return "a value"

# thing = somefunction()
# print(thing)


def exp(num1, num2):
    total = num1 ** num2
    return total

big_number = exp(33, 6)
print(big_number)