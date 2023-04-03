print(",".join(["a", "b", "c"])) # łączy do siebie ale rozdziela argumentem
print("Witaj Świecie".replace("Witaj", "Cześć")) # zamieniamy Witaj na Cześć
print("To jest zdanie".startswith("To")) # "To jest zdanie" rozpoczyna się od "To" więc wynik jest prawdą(True)
print("To jest zdanie".endswith("nie")) # "To jest zdanie" kończy sie na "nie" więc wynik jest prawdą(True)
print("j" in "To jest zdanie") # czy "j" znajduje się w "To jest zdanie". tak więc wynik jest prawda
print("To jest zdanie".upper()) # .upper zamienia na duże litery
print("To jest zdanie".lower()) # .lower zamienia na małe litery

print("---------")
lista = [10, 20, 25, 36, 40]

if all([i % 2 == 0 for i in lista]):     # sprawdza czy wszystkie liczby są parzyste
    print("Wszystkie liczby parzyste")

if any([i % 2 == 0 for i in lista]):    # jesli choć jedna jest parzysta
    print("Chociaż jedna parzysta")

for i in enumerate(lista):   # numeruje liste od zera
    print(i)

for i in enumerate(lista):
    print(i[0] + 1, i[1])   # numerowanie listy zaczyna się od 1