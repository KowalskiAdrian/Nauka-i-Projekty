import re

wynik = re.match(r"^Hello World$", "Hello World")

if wynik:
    print("Dopasowano!")
else:
    print("Nie dopasowano") 

wynik = re.match(r"^(Hello) (World)$", "Hello World") # utworzono dwie grupy (Hello) (World)
wynik = re.match(r"^(Hello) (Wor(ld))$", "Hello World") # utworzono trzy grupy (Hello) (World)+(ld)=(Wor(ld)

if wynik:
    print("Dopasowano!")
    print(wynik.group())
    print(wynik.group(0))
    print(wynik.group(1))
    print(wynik.group(2))
    print(wynik.group(3))
    print(wynik.groups())
else:
    print("Nie dopasowano") 