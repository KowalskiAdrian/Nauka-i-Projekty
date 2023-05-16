class Animal:
    fur_color = "Orange"
    
    def speak(self):
        raise NotImplementedError
        
    
    def eat(self):
        print("Lovley Fish!!!")
    
    def chase(self, animal="gazzele"):
        print("I am chasing a", animal)
    
class HouseCat(Animal):
    def speak(self):
        print("Meeeeoowww")

    def eat(self):
        super().eat()
        print("I am eating salmon")

    def chase(self, animal):
        super().chase(animal)
        print(animal, "was caught")

cat = HouseCat()
cat.chase("mouse")