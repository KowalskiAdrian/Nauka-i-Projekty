wiek = 19
kasa = 40

if wiek >= 18:                             # jeśli wiek jest większy lub równy 
    if kasa >= 35:                         # jeśli kasa jest większy lub równy
        print("możesz wejść")              # wydrukuj możesz wejść

if wiek >= 18 and kasa >= 35:             # operator "and" połącza operatory "if"
    print("możesz wejść")

if wiek >= 12 or kasa >= 30:              # brak dwukropka (or-lub) jedna prawda wystarczy do wejścia 
    print("możesz wejść")

if not wiek >= 11 or kasa >= 10:           # operator zaprzeczenia(if not zaprzeczenie)  jedna prawda wystarczy do wejścia
    print("możesz wejść")
else:
    print("Nie możesz wejść")

if True or False and False:               # kolejnośc wykonywania działan operator and jest pierwszy 
    print("Prawda")
else:
    print("Fałsz")

#if (True or False) and False:              # operator and jest drugi
#    print("Prawda")
#else:
#    print("Fałsz")


