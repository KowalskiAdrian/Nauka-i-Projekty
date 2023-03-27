def func(x):
    return x * x           # mnożenie x*x

zmienna = func
print(zmienna(5))          # dodajemy zmenną x=5 otrzymujemy wynik z zadania 5*5=25

def func2(f1, x):           
    return f1(x) * x       # jako argument posyłamy inną funkcje

print(func2(func, 5))      # podnosimy funkcje do sześcianu   5*5*5=125

def silnia(x):                       # silnia wzór !3 = 3 * 2 * 1 = 6     !5 = 5 * 4 * 3 * 2 * 1 = 120
    if x <= 1:                       # jeśli x(silnia) jest mniejsze lub równe 1 to 
        return 1                     # zwróć 1
    else:                            # w przeciwnym razie 
        return x * silnia(x - 1)     # zwróć x*(x-1)

print(silnia(5))                     # zwróć  !5=5x4x3x2x1=120                           
print(silnia(4))                     # zwróć  !4=4x3x2x1=24
print(silnia(2))                     # zwróć  !2=2x1=2
print(silnia(1))                     # zwróć  !1=1
print(silnia(9))                     # zwróc  !9=9x8x7x6x5x4x3x2x1=362.880
