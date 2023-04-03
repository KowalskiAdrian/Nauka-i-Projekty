lista = ["Subskrybuj", "Kanał", "O", "Wszystkim", ]

i = 0
while i < len(lista):            # len(lenght) Długość, pętla nieobiektowa wydruk obiektów po koleji
    print(lista[i])
    i += 1

for x in lista:                  # for czyli przez zmienną x w(in) lista, pętla obiektowa
    print(x)                     # wydruk listy po koleji


print(list(range(10)))           # wydrukuje zakres(range) od 0 do 9 (10 liczb liczymy od zera czyli "9" jest ostatnie) 

for y in range(1, 11):           # wydrukuj zakres(range od 1 do 11)zaczyna od 1 kończy na 10 
    print(y)


for y in range(1, 11, 2):           # trzeci argument(2) to skok czyli wyświetli co 2 czyli 1,3,5,7,9
    print(y)