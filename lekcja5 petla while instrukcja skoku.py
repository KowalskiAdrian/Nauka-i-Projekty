#i = 0

#while i < 5:                               # wukonujemy pętle która konczy sie na 4 licza
#    print(i)
#    i += 1                                 # dzęki tej linijce pętla się nie zapętla
#print("Koniec")


#i = 0

#while i < 5:
#    print(i)                               # zapętlenie pętli
#print("Koniec")

#i = 0

#while True:
#    print(i)                               # zapętlenie pętli
#    i += 1
#    if i >= 5:
#        break                              # złam przerwij(zakończenie pętli)
#print("Koniec")


i = 0

while True:
    i += 1
    if i % 2 == 1:                          # zwróć liczby parzyste operator %
        continue                            # kontynuuj(instrukcja skoku)
    print(i)                                # zapętlenie pętli
    if i > 10:                              # koniec na pierwszej parzystej czyli 12
        break                               # złam przerwij(zakończenie pętli)(instrukcja skoku)
print("Koniec")

