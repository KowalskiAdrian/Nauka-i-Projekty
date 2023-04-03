plik = open("tekst.txt", "r" )
tekst =plik.read()
plik.close

def policz(txt, znak):
    licznik = 0
    for z in txt:
        if z == znak:
            licznik += 1
    return licznik

print(policz(tekst, "a"))                         # liczenie tylko małych liter "a"

print(policz(tekst, "a") + policz(tekst, "A"))    # liczenie małych i dużych liter "A"
print(policz(tekst, "w") + policz(tekst, "W"))    # liczenie małych i dużych liter "W"
print(policz(tekst, "w"))                         # liczenie małych liter "W"
print(policz(tekst.lower(), "w"))                 # liczenie małych i dużych liter "W"

for w in "abcdefghijklmnoprstuwxyz":
    ile = policz(tekst.lower(), w)
    procent = 100 * ile / len(tekst)
    print("{0} - {1} - {2}%".format(w.upper(), ile, round(procent, 2)))    # obliczenie na ile procent pojawia sie literka