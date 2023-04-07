Fav_foods = ['Pizza', 'Tacos', 'Salmon']
Fav_foods = set(Fav_foods)

for food in Fav_foods:
    if food == "Salmon":
        size = input("What the size of salmon would you like?")
        print(f"You ordered a {size} salmon")
    
    
food = "Pizza!"
for letter in food:
    print(letter)
    
    
person = {
    "name": "Adrian",
    "twitter": "@007__Adrian",
    "instagram": "niemamkonta"
}
for key, value in person.items():
    print(f"The key is {key} and the value is {value}")