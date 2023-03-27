zmienna = 1
zmienna2 = "Abc"

lista = [1, 2, "c", "d", "e", ]      # liczymy od zera czyli 0,1,2,3,4. String- ciąg liczb i liter
print(lista)
print(lista[4])

lista[2] = 3                         # zamiana drugiego znaczka na 3 czyli c=3
print(lista)

tekst = "Hello world"
print(tekst[1])                      # [1] oznacza (drugą) litere w tekscie "hello world"
print(lista + ["f", "g"] )           # dodajemy ale nie dołączamy elementy do listy
print(lista * 3)                     # mnożenie listy bez dołączonych elementów
print("Ilość elementów: ", len(lista))

lista.append("f")                    # apennd czyli dołącz na koniec listy      
print(lista)

lista.append(["g", "h"])
print(lista)
print(lista[6][1])

lista.insert(3, 3)     # insert czyli dodaj do listy. pierwsza liczba mówi na które miejsce druga mówi co dodajemy 
print(lista)
print("Ilość: ", lista.count(3))     # zliczanie(count) mówi ile jest "3" w liście czyli 2 
print("Indeks:", lista.index("f"))   # index mówi na której pozycji jest "f"

lista.remove("f")                    # usuwanie z listy 
print(lista)

lista2 = [1, 20, 35, -5, 0]
print("min: ", min(lista2))          # minimum na liście "-5"
print("max: ", max(lista2))          # maksimum na liście "35"

lista2.sort()                        # sortowanie 
print(lista2)

lista2.reverse()                     # odwrócona kolejność sortowania
print(lista2)

lista2.clear()                       # wyczyszczenie(clear) listy
print(lista2)
