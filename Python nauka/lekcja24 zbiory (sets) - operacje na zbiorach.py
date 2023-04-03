liczby1 = {0, 1, 2, 4}     # zbiór liczb
slowa = set(["a", "b", "c"])  #zmienna słowa

print(liczby1)          
print(slowa)      # pokazuje zmienną ale nie zawsze po kolei

liczby1.add(5)    # dodajemy do zbioru "liczby1"  "5" 
print(liczby1)
liczby1.remove(0)  # odejmujemy z zbioru "liczby1"  "0"
print(liczby1)

liczby1.add(5)    # jeszcze raz dodajemy do zbioru "liczby1"  "5" 
print(liczby1)    # w zbiorach wartości się nie powtarzają więc nie dodamy następnej "5"

print(1 in liczby1)   # sprawdzenie czy dana wartość znajduje się w zbiorze "1"  TRUE/FALSE
print("a" in liczby1)   # sprawdzenie czy dana wartość znajduje się w zbiorze "a"  TRUE/FALSE


liczby1 = {0, 1, 2, 4, 4}
liczby2 = {3, 4, 5, 6} 

print(liczby1 | liczby2)  # kreska  "|" znaczy lub. daje to sume dwóch zbiorów bez powtarzania znaków
print(liczby1 & liczby2)  # operator "&" powoduje wypisanie tylko tych samych licz ze zbiorów
print(liczby1 - liczby2)  # operator "-" od zioru jeden odejmujemy zbiór dwa
print(liczby2 - liczby1)
print(liczby1 ^ liczby2)  # różnica symetryczna odejmujemy od liczb. wynik to liczby które się nie powtórzyły