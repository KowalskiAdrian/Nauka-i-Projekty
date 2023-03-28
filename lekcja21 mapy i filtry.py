liczby = [2, 10, 12, 15, 20, 25, 30, 35]

# Mapy

def funkcja(x):
    return x * 2               # kazdy argument zosta pomnorzony x2

wynik = map(funkcja, liczby)
print(list(wynik))             # dodajemy "list" by otrzymac wynik

wynik2 = map(lambda x: x +2, liczby)    # do kazdego argumentu dodajemy dwa
print(list(wynik2))

# Filtry               funkcja zwraca nam tylko TRUE lub FALSE

wynik3 = filter(lambda x: x - 1, liczby)
