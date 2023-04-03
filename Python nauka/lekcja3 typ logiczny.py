x = True
y = False                            #piszemy z dużej litery
print(x)
print(y)

print(5 == 5) # True                 # sprawdzamy czy 5 równa jest 5 wynik true
print(5 == 1) # False               

print(5 != 1) # True                 # !-operator różne prawda
print(5 != 5) # False                # !-operator różne fałsz

print(5 > 5) # False`                # operator większe
print(5 > 3) # True                  

print(5 <= 3) # False                # mniesjcze lub równe
print(5 >= 3) # True                 # wieksze lub równe

if 5 == 5:         #(jeżeli 5 rowna się 5 wydrukuj prawda po czym wydrukuj koniec) if sprawdza True czy False, konczymy dwukropkiem
    print("Prawda")
print("Koniec")

if 15 > 10:                            # if sprawdza True czy False, konczymy dwukropkiem
   print("Większe")                    # wydrukuj większe jesli True
else:                                  # w przeciwnym razie                else:
    print("Mniejsze")                  # wydrukuj miejsze

x = 10
y = 15

if x > y:
    print("X większe Y")
elif x < y:                             # elif to else if razem kolejny warunek 
    print("X mniejsze Y")
else:                                   # w przeciwnym razie
    print("X równe Y")                  # drukuje pierwszą prawde dostępną czyli elif "X mniejsze Y"





