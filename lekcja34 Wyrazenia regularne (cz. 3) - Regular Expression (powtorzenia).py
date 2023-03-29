import re

if re.match("[A-Z][a-z]", "Al"):      # kolejność dopasowywania(dopasowano)
    print("Dopasowano!")
else:
    print("Nie dopasowano!")


if re.match("[A-Z][a-z]", "aL"):      # kolejność(niedopasowano)
    print("Dopasowano!")
else:
    print("Nie dopasowano!")

if re.match("^[A-Z][a-z]$", "aL"):      # kolejność(niedopasowano)
    print("Dopasowano!")
else:
    print("Nie dopasowano!")

if re.match("^[A-Z][a-z]$", "Al"):      # poczátek i koniec(dopasowano)
    print("Dopasowano!")
else:
    print("Nie dopasowano!")

if re.match("^[A-Z][a-z]$", "Alt"):      # poczátek i koniec(niedopasowano)
    print("Dopasowano!")
else:
    print("Nie dopasowano!")

if re.match("^[A-Z][a-z]*t$", "Alt"):      # *t dodaje litere t na 3 miejsce(dopasowano)
    print("Dopasowano!")
else:
    print("Nie dopasowano!")

if re.match("^[A-Z][a-z]*$", "Alt"):      # *  random dodaje litere na 3 miejsce(dopasowano)
    print("Dopasowano!")
else:
    print("Nie dopasowano!")
    

if re.match("^[A-Z][a-z]+t$", "Alt"):      # + dodaje litere t na 3 miejsce(dopasowano)
    print("Dopasowano!")
else:
    print("Nie dopasowano!")

if re.match("^[A-Z][a-z]+$", "Al"):      # + dodaje litere t na 3 miejsce(dopasowano nawet podzas braku)
    print("Dopasowano!")
else:
    print("Nie dopasowano!")

if re.match("^[A-Z][a-z]?[a-z]$", "Alt"):      # ? moze ale nie musi wystápi w przedziale
    print("Dopasowano!")
else:
    print("Nie dopasowano!")

if re.match("^[A-Z][a-z]?[a-z]$", "Alllllt"):  # ?  nie dopuszcza  wystąpienia w przedziale takich samych znaków
    print("Dopasowano!")
else:
    print("Nie dopasowano!")
    
if re.match("^[A-Z][a-z]{2,5}$", "Alt"):      # dopuszczamy od2 do 5 liter (dopasowano)
    print("Dopasowano!")
else:
    print("Nie dopasowano!")

if re.match("^[A-Z][a-z]{2,5}$", "A"):      # dopuszczamy od2 do 5 liter(niedopasowano)
    print("Dopasowano!")
else:
    print("Nie dopasowano!")

if re.match("^[A-Z][a-z]{2,}$", "Sebastian"):      # dopuszczamy od 2 liter(dopasowano)
    print("Dopasowano!")
else:
    print("Nie dopasowano!")

if re.match("^[A-Z][a-z]{,5}$", "Sebastian"):      # dopuszczamy do 5 liter(niedopasowano)
    print("Dopasowano!")
else:
    print("Nie dopasowano!")


    