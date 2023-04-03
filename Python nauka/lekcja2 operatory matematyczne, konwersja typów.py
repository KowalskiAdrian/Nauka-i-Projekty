print("kolejność:")
print((2 + 2) * 2)         # przeciągamy pierszeństwo nawiasami (kolejność)
print("dzielenie:")
print(5 / 2)               # tylko całe liczby
print(5 // 2)              # liczby po przecinku , z resztą
print("mnożenie:")
print(2 * 3)
print(2 ** 3)              # potęgowanie
print("skrócone:")
x = 5
x = x + 1
print(x)                   # dodaje 1 do wyniku
x += 1                     # dodanie 1 do juz istniejącego wyniku z poprzedniego działania
print(x)
                                  # x++ błąd
print("Konwersja:")
a = input("Podaj 1 liczbę: ")
b = input("Podaj 2 liczbę: ")
print( a + b)                     # liczby doklejają sie do siebie np. 2+3=23
print(int(a) + int(b))            # wynik nie uwzględnia dziesiętnych  INTIGER liczby całkowite


a = input("Podaj 1 liczbę: ")
b = input("Podaj 2 liczbę: ")
print(float(a) + float(b))        # wynik uwzględnia dziesiętne np. 2.3+2.3=4.6
y = 2
z = 2
print(y + z)                      # wynik 4
print(str(y) + str(z))            # wynik 22 dokleja 
del y
print(str(y) + str(z))            # błąd
