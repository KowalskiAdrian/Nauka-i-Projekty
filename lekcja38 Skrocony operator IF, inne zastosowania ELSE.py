print("Prawda")  if 5 > 2 else print("Nieprawda")     # funkcja jednolinijkowa
a = "Parzysta"  if 10 % 2 == 0 else print("Nieparzysta")     
print(a)
b = "Parzysta"  if 5 % 2 == 0 else print("Nieparzysta") 


for i in range(10):
    if i > 5:
        continue          # kontynułujemy pętle
    
else:
    print("Koniec")
        
try:
    a = 5/0
except ZeroDivisionError:       # dzielimy przez 0 Błąd
    print("Błąd")
else:                        
    print("Koniec")
finally:
    print("Zawsze")
