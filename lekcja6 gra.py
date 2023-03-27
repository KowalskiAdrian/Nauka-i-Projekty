from random import randint

#for i in range(100):                     #sprawdzanie czy działa kod
#    print(randint(1,10))

los = randint(1,100)
odp = -1                                  # odpowiedz -1 jest poza skalą po to by nie podać wyniku
i = 0                                     # zliczanie obiegów pętli
print("zgadnij liczbe z przedziału  1 - 100")

while odp != los:
    i += 1
    odp = int(input("Podaj liczbe: "))
    if odp > los:                         # odpowiedz jest większa
        print("Wylosowana liczba jest mniejsza od Twojej")
    elif odp < los:                       # odpowiedz jest mniejsza
        print("Wylosowana liczba jest większa od Twojej")
print("Brawo odgadłeś za", i, "razem.")   #dobra odpowiedz



