my_thing = False

if not my_thing:
    print("Print a statment in here")
    
    
name = "Barbarossa"
if name not in ['Adrian', 'Peter', 'Lucas']:
    print("Barbarossa is not part of the club")
    
    
name1 = "Adrian"
name2 = "Lucas"
if name1 is not name2:
    print("Different names")

s = ["Adrian", "Lucas"]
name2 = "Lucas"
if s is not name2:
    print("Different names!")

lst = ["Adrian", "Lucas"]
name2 = ["Adrian", "Lucas"]
if name in lst is not name2:
    print("Different names!")
else:
    print("That the same names")

    