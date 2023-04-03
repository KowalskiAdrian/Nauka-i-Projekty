def gen():
    i = 0
    while i < 5:       # wywołanie pętli
        yield i        # "yield" wykonuje się w pętli wiele razy do konca
        i += 1

for i in gen():
    print(i)                        # obiekt do iterowania pętli obiektowej

print(gen())                        # otrzymujemy wynik w podpunktach 5 elementów licząc od zera


def gen():
    i = 0
    while i < 5:       # wywołanie pętli
        yield i        # "yield" wykonuje się w pętli wiele razy do konca
        i += 1

for i in gen():
    print(i)                        # obiekt do iterowania pętli obiektowej

print(list(gen()))                  # otrzymujemy wynik w liście i kwadratowych nawiasach


def parzyste(x):
    i = 0
    while i <= x:
        if i % 2 == 0:
            yield i     # yield zwróci wynik ale nie skończy funkcji
        i += 1

for i in parzyste(16):  
    print(i)            # wynik plus rezta funkcji w nowej lini      


  
print(list(parzyste(30)))  # wynik z 30 plus reszta funkcji w nawiasie kwadratowym

                 
