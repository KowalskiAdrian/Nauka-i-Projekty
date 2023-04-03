class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):           # podajemy klase po której dziedziczymy czyli "Animal"
    def voice(self):         # dodajemy "voice" czyli głos
        print("How How")

class Wolf(Dog):             # następuje dziedzicenie po klasie "dog" głosu
    def getVoice(self):      # dodajemy def "getVoice" by głos się nie nałożył i dodajemy głos wilka 
        print("Jestem Wilkiem,")
        super().voice()

class Cat(Animal):           # dodajemy do klasy "Animal" kota "cat"
    def getVoice(self):
        print("Meow Meow")

dog = Dog("Reksio", 10)      # wywołujemy z klasy "Animal" psa "dog" 
print(dog.name)              # imie
print(dog.age)               # wiek
dog.voice()                  # głos

cat = Cat("Tom", 13)         # wywołujemy z klasy "Animal" kota "cat" 
cat.getVoice()               # głos

wolf = Wolf("Geralt", 55)    # wywołujemy z klasy "Animal" wilka
wolf.getVoice()              # głos
print(wolf.name)             # imię