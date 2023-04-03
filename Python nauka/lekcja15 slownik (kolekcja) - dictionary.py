slownik = {1: "Poniedziałek", 2: "Wtorek", 7: "Niedziela" } # nie liczymy od zera

print(slownik[1])                # indeks przypisany jest tutaj do 1,2,7
print(slownik[7])
slownik[3] = "Środa"             # dodajemy element na koniec listy
slownik[4] = False
slownik[5] = 5
slownik["a"] = 1
print(slownik["a"])
print(slownik)

#print(slownik[8])
print(slownik.get(8, "Inny Dzień"))

print("\nPętla:")          # wyświetl slownik linijka po linijce
for l in slownik:
    print(l)

print("\n---------")
print(slownik.pop(1))
print(slownik)

