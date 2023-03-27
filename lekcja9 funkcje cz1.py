def funkcja_test():
    print("Funkcja!")

funkcja_test()          # wywołanie funkcji
funkcja_test()          # wywołanie funkcji
funkcja_test()          # wywołanie funkcji
funkcja_test()          # wywołanie funkcji

def dodaj(x):           # dodajemy argument "x" do funkcji, kończymy funkcje dwukropkiem
    print(x + 1)

zmienna = dodaj(2)     # (zmienna = + (2))  dodajemy wartość dla argumentu x=2
print(zmienna)         # drukuj zmienna czyli 2+1=3 

def dodaj(x, y):       # dodajemy dwa argumenty do siebie , kończymy dwukropkiem   
    print(x + y)

dodaj(2, 3)            # x=2 y=3

def dodaj(x, y = 1):       # dodajemy wartość do argumentu y=1   
    print(x + y)

dodaj(2, 3)                # wynik 5
dodaj(2)                   # wynik po dodaniu wartości y=1 daje wynik 3

def dodaj(x, y = 1, z =0):       # dodajemy wartość do argumentu y=1  z=0
    print(x + y + z)

dodaj(2, 3)                # wynik 5
dodaj(2)                   # wynik po dodaniu wartości y=1, z=0 daje wynik 3
dodaj(2, 3, 5)             # 2+3+5=10           

def dodaj(x, y = 1, z = 0):
  print("Czy ja istnieje?")
  return x + y + z        # Dodajemy return zamiast print

print(dodaj(2, 3))        # dodajemy print i nawias by otrzymać wynik 5
print(dodaj(2))           # dodajemy print i nawias by otrzymać wynik 3
wynik = dodaj(2, 3, 5)    # wynik plus dodaj  
print(wynik)              # print(wynik) aby pokazac wynik 10