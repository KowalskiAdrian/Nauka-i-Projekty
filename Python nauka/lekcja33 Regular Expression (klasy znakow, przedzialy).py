import re

if re.match("\?", "Kot"):   # sprawdzenie czy  jest to samo(niedopasowanie)
    print("Dopasowano")     
else:
    print("Niedopasowano!")

if re.match("Kot", "Kot"):  # sprawdzenie czy  jest to samo(dopasowane)
    print("Dopasowano")
else:
    print("Niedopasowano!")

if re.match("Ko.", "Kot"):  # sprawdzenie z kropką czy  jest to samo(dopasowane)
    print("Dopasowano")
else: 
    print("Niedopasowano!")

if re.match("^Ko.$", "Kot"):  # ^ rozpoczęcie wyrazenia  $ zakończenie wyrazenia(dopasowane)
    print("Dopasowano")
else: 
    print("Niedopasowano!")

if re.match("^Ko.$", "Kotttttt"):  # ^ rozpoczęcie wyrazenia  $ zakończenie wyrazenia(niedopasowane)
    print("Dopasowano")
else: 
    print("Niedopasowano!")

if re.match("^Ko.$", "Koń"):  # ^ rozpoczęcie wyrazenia  $ zakończenie wyrazenia(dopasowane)
    print("Dopasowano")
else: 
    print("Niedopasowano!")

if re.match("^[Kk]o.$", "Koń"):  # [Kk] możliwe dopasowanie małej lub dużej litery
    print("Dopasowano")
else: 
    print("Niedopasowano!")

if re.match("^[A-Z]o.$", "Rot"):  # [A-Z]  litery z przedziału dużych liter(dopasowane)
    print("Dopasowano")
else: 
    print("Niedopasowano!")

if re.match("^[A-Za-z]o.$", "Rot"):  # [A-Za-z]  litery z przedziału dużych i  małych liter(dopasowane)
    print("Dopasowano")
else: 
    print("Niedopasowano!")

if re.match("^[^A-Za-z]o.$", "Rot"):  # [^A-Za-z]  symbol daszku neguje przedział(niedopasowane)
    print("Dopasowano")
else: 
    print("Niedopasowano!")

if re.match("^[Rr]ok[-_=][0-9][0-9][0-9][0-9]$", "Rok-1984"):  # (dopasowane)
    print("Dopasowano")
else: 
    print("Niedopasowano!")

    