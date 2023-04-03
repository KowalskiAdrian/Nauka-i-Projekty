# Python  https://www.python.org/downloads/
# Visual Studio Code  https://code.visualstudio.com
# W zakładce "extensions" zainstalować plugin do Pythona
# W terminalu: pip install requests

# Szybki kurs korzystania z Visual Studio Code
# 1) boczny panel
# 2) edytor kodu
# 3) terminal

### W terminalu:
# python program.py
# clear
# pip install requests
### A cała reszta dzieje się w edytorze kodu

# funkcja(argument1, argument2)

# imiona = ["ala", "wojtek", "alina"]
# print(imiona)
# print(imiona[1])  # ==> wojtek

# paczka = {
#     'imie': 'jan',
#     'nazwisko': 'kowalski'
# }
# print(paczka)
# print(paczka['nazwisko'])  # ==> kowalski

# osoby = [
#     {'imie': 'jan', 'nazwisko': 'kowalski'},
#     {'imie': 'anna', 'nazwisko': 'wisniewska'}
# ]
# print(osoby)
# print(osoby[1]['nazwisko'])  # ==> wisniewska

# dane = {
#     "table": "A",
#     "currency": "dolar amerykański",
#     "code": "USD",
#     "rates": [
#         {
#             "no": "193/A/NBP/2022",
#             "effectiveDate": "2022-10-05",
#             "mid": 4.8380
#         }
#     ]
# }

# http://api.nbp.pl/api/exchangerates/rates/a/usd/2022-10-05/?format=json

# from szuflada import wiertarka
from requests import get

print("KALKULATOR WALUT")

waluta = input("Podaj walutę: ")

data = input("Podaj datę (RRRR-MM-DD): ")

odpowiedz = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{data}/?format=json")

dane = odpowiedz.json()

kurs = dane["rates"][0]["mid"]

print(f"1 {waluta} = {kurs:.2f} PLN")

