class Czlowiek:
    def __init__(self, imie):
        self.imie = imie
    
    def przedstaw(self):
        print("Nazywam się " + self.imie)
        
    @classmethod          # klasa ma użyteczną metode
    def nowy_czlowiek(cls, imie):   # dzięki "cls" możemy odwołać się do klasy
        return cls(imie)
    
    @staticmethod                # metoda statyczna
    def przywitaj(arg):
        print("Cześć " + arg)


# można wywołac metode bez obiektu
cz1 = Czlowiek.nowy_czlowiek("Sebastian")
cz1.przedstaw()
cz2 = cz1.nowy_czlowiek("Adrian")
cz2.przedstaw()

Czlowiek.przywitaj("przyjacielu!")
cz2.przywitaj("Człowieku")