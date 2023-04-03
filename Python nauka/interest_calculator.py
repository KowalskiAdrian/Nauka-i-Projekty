# Kalkulator płatności odsetek

# pobranie wartości początkowej kapitału, stopę procentową i liczby lat
poczatkowy_kapital = float(input("Podaj wartość początkową kapitału: "))
oprocentowanie = float(input("Podaj stopę procentową: "))
liczba_lat = int(input("Podaj liczbę lat: "))

# wyliczenie wartości końcowej kapitału
wplata_roczna = 0 # wartość początkowa
for rok in range(liczba_lat):
    wplata_roczna += float(input(f"Podaj wartość wplaty dla {rok+1} roku: "))
    # dodajemy wartość wpłat na początku każdego roku
    poczatkowy_kapital += wplata_roczna
    poczatkowy_kapital += poczatkowy_kapital * oprocentowanie / 100
    # dodajemy odsetki na koniec każdego roku

# wyświetlenie wyniku
print(f"Wartość końcowa kapitału: {poczatkowy_kapital:.2f}")
