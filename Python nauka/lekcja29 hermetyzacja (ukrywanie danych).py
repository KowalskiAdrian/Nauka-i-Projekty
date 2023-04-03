class Test:
    lista = []
    def dodaj(self, arg):
        self.lista.append(arg)    
        
    def zdejmij(self):
        if len(self.lista) > 0:
            return self.lista.pop(len(self.lista) -1)
        else:
            return
        
obj = Test()
obj.dodaj("A")
obj.dodaj("B")
obj.dodaj("C")
print(obj.zdejmij())
print(obj.lista)

# ukrywanie hermetyzacja

class Test:
    _lista = []                # dodajemi kreske dolną _ do lista by stała się prywatna 
    def dodaj(self, arg):
        self._lista.append(arg)    
        
    def zdejmij(self):
        if len(self._lista) > 0:
            return self._lista.pop(len(self._lista) -1)
        else:
            return
        
obj = Test()
obj.dodaj("A")
obj.dodaj("B")
obj.dodaj("C")
print(obj.zdejmij())



class Test:
    __lista = []                # dodajemy dwie kresk dolne __ do lista by stała się  jeszcze bardziej prywatna
    def dodaj(self, arg):
        self.__lista.append(arg)    
        
    def zdejmij(self):
        if len(self.__lista) > 0:
            return self.__lista.pop(len(self.__lista) -1)
        else:
            return
        
obj = Test()
obj.dodaj("A")
obj.dodaj("B")
obj.dodaj("C")
obj._Test__lista.append("X")  # odwołujemy się do listy przez klase
print(obj.zdejmij())
print(obj._Test__lista)
