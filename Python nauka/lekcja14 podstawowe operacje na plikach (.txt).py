plik = open("test.txt", "w")       # "w" oznacza zapis z czyszczeniem poprzedniej zawartości
if plik.writable():
    plik.write(input("Wprowadz tekst: ") + "\n")
plik.close()

#plik = open("test.txt", "r")       # "r" readable - do odczytu

#if plik.readable():
#    print("Zawartość pliku:")
#    tekst = plik.read()
#    print(tekst)


#plik = open("test.txt", "a")       # "a"(append) oznacza dopis do poprzedniej zawartości
#if plik.writable():
#    plik.write(input("Wprowadz tekst: ") + "\n")        
#plik.close()

#plik = open("test.txt", "r")

#if plik.readable():
#    print("Zawartość pliku:")
#    tekst = plik.read()
#    print(tekst)


#plik = open("test.txt", "a")       # "a" oznacza zapis z dodaniem  do poprzedniej zawartości
#if plik.writable():                 
#    plik.write(input("Wprowadz tekst: ") + "\n")
#plik.close()

#plik = open("test.txt", "r")

#if plik.readable():
#    print("Zawartość pliku:")
#    tekst = plik.readlines()
#    print(tekst)
#    for l in tekst:                # l - wypisywanie linijka po linijce
#        print(l)

plik = open("test.txt", "a")       # "a" oznacza zapis z dodaniem  do poprzedniej zawartości
if plik.writable():
    plik.write(input("Wprowadz tekst: ") + "\n")
plik.close()

plik = open("test.txt", "r")

if plik.readable():
    print("Zawartość pliku:")
    for l in plik:
        print(l)

