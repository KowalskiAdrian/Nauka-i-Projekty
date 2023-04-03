class Test:
    def __new__(cls):
        print("Hello Class")
        
obj = Test()


class Test:
    def __del__(self):         # metoda detruktor wykonuje się na końcu i czyści pamięć która nie jest potrzebna
        print("Bye Class")
        
obj = Test()    # obiekt kończy istnienie kiedy nie posiada żadnej referencji


print("Koniec")  # "Koniec" jest przed "Bye Class"


class Test:
    def __del__(self):         # metoda detruktor wykonuje się na końcu i czyści pamięć która nie jest potrzebna
        print("Bye Class")
        
obj = Test()    # obiekt kończy istnienie kiedy nie posiada żadnej referencji
del obj         # delete "del" kasuje obj i wyswietla "koniec" na końcu

print("Koniec")


class Test:
    def __del__(self):         # metoda detruktor wykonuje się na końcu i czyści pamięć która nie jest potrzebna
        print("Bye Class")
        
obj = Test()    # obiekt kończy istnienie kiedy nie posiada żadnej referencji
obj2 = obj      # obiekt posiada uchwyt przez co "Bye Class" występuje na końcu
del obj         

print("Koniec")




class Test:
    def __del__(self):         # metoda detruktor wykonuje się na końcu i czyści pamięć która nie jest potrzebna
        print("Bye Class")
        
obj = Test()    # obiekt kończy istnienie kiedy nie posiada żadnej referencji
obj2 = obj      # obiekt posiada uchwyt przez co "Bye Class" występuje na końcu
lista = [obj2]  # uchwyt
del obj         
del obj2
del lista[0]         

print("Koniec")