def decorator(func):     #dekorator przyjmie jeden argument ktory przyjmie postac funkcji(zdobienie)
    def wrapper():       # wrapper opakowywuje nastepną funkcje
        print("-------")   # ozdabiamy przed 
        func()
        print("-------")    # ozdabiamy po
    return wrapper

def hello():
    print("Hello World")

hello = decorator(hello)    # dekorator hello wypełni funk() w nawiasie naszym "Hello World"
hello()

@decorator                  # funkcja stanie sie udekorowana dzieki "@"
def witaj():
    print("Witaj Swiecie")

witaj()