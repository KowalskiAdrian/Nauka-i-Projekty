def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Wybierz operację.")
print("1.Dodaj")
print("2.Odejmij")
print("3.Pomnóż")
print("4.Podziel")

# pobieranie wejścia od użytkownika
wybor = input("Wybierz operację (1/2/3/4): ")

num1 = float(input("Podaj pierwszą liczbę: "))
num2 = float(input("Podaj drugą liczbę: "))

if wybor == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif wybor == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif wybor == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif wybor == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("Błędna wartość")
