class Czlowiek:
    imie = "Sebastian"  # początek kodu klasy, działa jak funkcja 

    def przedstawSie(self):    # self własna klasa
        return "Cześć, mam na imię " + self.imie # zwrot Cześć mam na imię + self.imie(Sebastian)


obiekt = Czlowiek()    # do obiektu jest przypisana klasa
print(obiekt.imie)
print(obiekt.przedstawSie())
obiekt2 = Czlowiek()
obiekt2.imie = "Adrian"   # zmiana wpływa tylko na ten obiekt
print(obiekt2.imie)
print(obiekt.przedstawSie())



class Czlowiek:
    imie = "Sebastian"  # początek kodu klasy, działa jak funkcja 

    def przedstawSie(self, powitanie = "Cześć"):    # self własna klasa, dopisujemy powitanie
        return powitanie + ", mam na imię " + self.imie    # zwraca nam powitanie + mam na imię + imię z klasy


obiekt = Czlowiek()    # do obiektu jest przypisana klasa
print(obiekt.imie)
print(obiekt.przedstawSie("Witam"))   # zamieniamy powitanie "Cześć" na "Witam"
obiekt2 = Czlowiek()
obiekt2.imie = "Adrian"   # zmiana wpływa tylko na obiekt2(imie)
print(obiekt2.imie)
print(obiekt.przedstawSie())



class Czlowiek:
    def __init__(self, imie, wiek):  # metoda pozwala zmienić domyślny konstruktor(dane wejściowe dla naszego obiektu)
        self.imie = imie
        self.wiek = wiek
        
    

    def przedstawSie(self, powitanie = "Cześć"):    # self własna klasa, dopisujemy powitanie
        return powitanie + ", mam na imię " + self.imie + " lat " + str(self.wiek) + "."   # zwraca nam powitanie + mam na imię + imię z klasy + lat + wiek


obiekt = Czlowiek("Sebastian", 24)    # do obiektu jest przypisana klasa
print(obiekt.imie)
print(obiekt.przedstawSie("Witam"))   # zamieniamy powitanie "Cześć" na "Witam"
obiekt2 = Czlowiek("Adrian", 18)
obiekt2.imie = "Adrian"               # zmiana wpływa tylko na ten obiekt
print(obiekt2.przedstawSie())