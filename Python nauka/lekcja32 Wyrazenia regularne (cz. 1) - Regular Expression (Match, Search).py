import re

wzor = "banan"    # \n nowa linia     \t tabulator
tekst = r"jablkobanananannasbanan"
print(re.match(wzor, tekst))      # "mach" sprawdzanie czy funkcja zaczyna się od danego wzoru

if re.match(wzor, tekst):     
    print("Dopasowano!")
else:
    print("Nie dopasowano!")
if re.search(wzor, tekst):        # search szuka w całości tekstu
    print("Dopasowano")
else:
    print("Nie dopasowano")    

wzor1 = r"banan\nbanan\tbanan"   # Raw surowy "r" traktuje całość jako jeden string    


print(wzor)
print(wzor1)
print(re.findall(wzor, tekst))   # funkcja findall czyli znajdz wszystkie


dopasowanie = re.search(wzor, tekst)
if dopasowanie:
    print(dopasowanie.group())   #funkcja grupy
    print(dopasowanie.start())   #funkcja start wskazuje początek dopasowania
    print(dopasowanie.end())   #funkcja koniec wskazuje koniec dopasowania
    print(dopasowanie.span())   #funkcja span wskazuje miejsce
    
    tekst2 =re.sub(wzor, r"Jagoda", tekst)  # sub zamiana szukania na "Jagoda"
    print(tekst2)