def funkcja(f, liczba):         # funkcja anonimowa lambda 
    return f(liczba)

print(funkcja(lambda x: x*x, 3))  

def kwadrat(x):            # funkcja lambda dziaa tu jak funkcja kwadrat
    return x * x
print(kwadrat(5))

wyn = (lambda x: x * x)(5)   # wywoanie funkcji lambda zaraz po jej deklaracji
print(wyn)

lam = lambda x: x * x
print(lam(5))
print(lam(4))


lam2 = lambda x, y: x * y       # operowanie z lambda na wiecej niz jednym argumecie
print(lam2(2, 3))               # funkcja lambda przypisana do dwuch argumentow 2x3=6
print((lambda x, y: x +y)(6, 5))   #dodawanie z funkcjá lambda