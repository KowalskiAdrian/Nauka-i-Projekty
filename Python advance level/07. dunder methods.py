class Animal:
    
    animal_type = "Unkown"
    
    def __init__(self, fur_color):
        self.fur_color = fur_color
        
    def speak(self):
        raise NotImplementedError
        
    def eat(self):
        print("Lovley Fish!!!")
    
    def chase(self, animal="gazzele"):
        print("I am chasing a", animal)
        
    def get_fur_color(self):
        print("Getting fur color:", self.fur_color)
    
class HouseCat(Animal):
    
    def __init__(self, fur_color):
        super().__init__(fur_color)
        print("Fur color was saved to the class Object")
        self.animal_type = "House cat"
        print(self.animal_type)
    
    def speak(self):
        print("Meeeeoowww")

    def eat(self):
        super().eat()
        print("I am eating halibut")

    def chase(self, animal):
        super().chase(animal)
        print(animal, "was caught")

cat = HouseCat("Purpure")
cat.get_fur_color()