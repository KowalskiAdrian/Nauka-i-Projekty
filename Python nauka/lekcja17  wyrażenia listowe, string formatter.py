lista = list(range(10))

print(lista)

nowa = [i * 2 for i in lista] # weż liste i każdy argumen "i" pomnóż przez 2
print("Nowa",nowa)

nowa2 = [i + 2 for i in lista if i % 2 == 0] # do wartości parzystych dodajemy 2
print("Nowa",nowa)
print("Nowa2",nowa2)

nowa2 = [i + 1 for i in lista if i % 2 == 0] # do wartości parzystych dodajemy 1
print("Nowa2",nowa2)

# Formatowanie String

argumenty = ["Sebastian", 24]   # postawiamy argumeny
tekst = "Cześć mam na imię {0} i mam {1} lat.".format(argumenty[0], argumenty[1])
print(tekst)
