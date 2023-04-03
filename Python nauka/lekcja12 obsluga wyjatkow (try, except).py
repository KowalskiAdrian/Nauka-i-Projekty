x = 12
y = 0

try:                                  # blok try czyli próbuj podzielić
    print(x / y)                     
    print("Linijka po")               # poczas błędu linijka sie nie wykona
except ZeroDivisionError:             # zastosowanie(wyrzucenie) wyjątku w punkcie błędu(ZeroDivisionError)
    print("Nastąpiło dzielenie przez 0!")     

print("Dalsze instrukcje...")


x = 12
y = 0

try:
    print(x + "!")        # pierwszy błąd
    print(x / y)
    print("Linijka po")
except ZeroDivisionError:
    print("Nastąpiłó dzielenie przez 0!")
except TypeError:                     # zastosowanie wyjątku drugiego omija reszte gdy jest błąd
    print("Błąd typu danych")
print("Dalsze instrukcje...")


x = 12
y = 0

try:
    print(x + "!")                                 # TypeError
    print(x / y)                                   # ZeroDivisionError
    print("Linijka po")                            # linijka się nie wykonuje przez błąd wyżej
except (ZeroDivisionError, TypeError):             # zastosowanie dwuch wyjątków 
    print("Wystąpił 1 z 2 błędów!")                # nie wiemy który błąd wystąpił

print("Dalsze instrukcje...")


x = 12
y = 0

try:
    lista = []                                     # błąd pusta lista
    print(lista[0])                                # IndexError
    print(x + "!")                                 # TypeError
    print(x / y)                                   # ZeroDivisionError
    print("Linijka po")
except (ZeroDivisionError, TypeError):             # zastosowanie dwuch wyjątków
    print("Wystąpił 1 z 2 błędów!")                # nie wiemy który błąd
except:
    print("Inny błąd")                             # generowanie nie wypisanych błędów
finally:
    print("FINNALY: Wykonam się i tak!")           # blok wykonuje obliczenia pomimo błedu
print("Dalsze instrukcje...")


x = 12
y = 2

try:
    lista = [3]
    print(lista[0])                                # IndexError brak
    print(x + 4)                                   # TypeError brak
    print(x / y)                                   # ZeroDivisionError brak
    print("Linijka po")                            # wykonuje się jeśli nie ma błędu
except (ZeroDivisionError, TypeError):             # zastosowanie dwuch wyjątków
    print("Wystąpił 1 z 2 błędów!")                # nie wiemy który błąd
except:
    print("Inny błąd")                             # generowanie nie wypisanych błędów
finally:
    print("FINNALY: Wykonam się i tak!")           # blok wykonuje obliczenia pomimo błedu lub braku błedu
print("Dalsze instrukcje...")

