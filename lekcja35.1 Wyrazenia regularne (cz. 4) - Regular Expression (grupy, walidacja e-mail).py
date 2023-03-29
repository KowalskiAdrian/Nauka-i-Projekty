import re

wynik = re.match(r"^Hello World$", "Hello World")

if wynik:
    print("Dopasowano!")
else:
    print("Nie dopasowano") 

wynik = re.match(r"^(Hello)( World)+$", "Hello World World World")  # spacja przed World by dopasowało do tekstu
                    # grupa nie nazwana
                               
if wynik:
    print("Dopasowano!")
    print(wynik.group())
    print(wynik.group(0))
    print(wynik.group(1))
    print(wynik.group(2))
    print(wynik.groups())
else:
    print("Nie dopasowano") 

wynik = re.match(r"^(He(?P<first>ll)o)( World)+$", "Hello World World World")  # dodajemy grupe first
                    # grupa nazwana
                               
if wynik:
    print("Dopasowano!")
    print(wynik.group())
    print(wynik.group(0))
    print(wynik.group(1))
    print(wynik.group(2))
    print(wynik.groups())
    print(wynik.group("first"))   # wywołana po nazwie etykiety
else:
    print("Nie dopasowano") 