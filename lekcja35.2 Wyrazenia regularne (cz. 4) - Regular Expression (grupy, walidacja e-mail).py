import re

wynik = re.match(r"^Hello World$", "Hello World")

if wynik:
    print("Dopasowano!")
else:
    print("Nie dopasowano") 

wynik = re.match(r"^((?:He)(?P<first>ll)o)( World)+$", "Hello World World World")  # spacja przed World by dopasowało do tekstu
                    
                               
if wynik:
    print("Dopasowano!")
    print(wynik.group())
    print(wynik.group(0))
    print(wynik.group(1))
    print(wynik.group(2))
    print(wynik.groups(3))
    print(wynik.group("first"))
else:
    print("Nie dopasowano") 


wynik = re.match(r"^((?:He)(?P<first>ll)o)( World)+(!|\.)$", "Hello World World World.")  # ! lub .
                    
                               
if wynik:
    print("Dopasowano!")
    print(wynik.group())
    print(wynik.group(0))
    print(wynik.group(1))
    print(wynik.group(2))
    print(wynik.groups(3))
    print(wynik.group("first"))
else:
    print("Nie dopasowano") 