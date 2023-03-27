#krotka = (2, 4, 8, 16, 32, 64, 128)
#print(krotka[0])
#print(krotka[6])
#print(krotka)

#print("Elemętów:", krotka.count(2))       #pierwszy przykład
#print("Index:", krotka.index(64))


#print(":\nWycinki:")
#print(krotka[0])




krotka = (2, 4, 8, 16, 32, 64, 128)
print(krotka)

print(":\nWycinki:")
print(krotka[0:3])
print(krotka[3:5])   # wycinamy z indeksu dwie liczby 16,32 zaznaczamy odkąd do kąd
print(krotka[3:6])   # wycinamy z indeksu trzy liczby 16,32, 64 zaznaczamy odkąd do kąd
print(krotka[0:100]) # wszystkie liczby z indeksu 2, 4, 8, 16, 32, 64, 128 zaznaczamy odkąd do kąd
print(krotka[-4:-2]) # zaczynamy odliczać (-4) od końca czyli 16 a (-2) liczymy jak by od zera czyli (0)128,(1)64,(2)32
print(krotka[0:7:2]) # dwa(2) oznacza wyknanie skoku czyli 2, 8, 32, 128