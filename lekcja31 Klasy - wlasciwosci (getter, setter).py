class KontoBankowe:
    __stan = 0
    
    @property               # własność jest tylko w stanie się odczytać
    def stan_konta(self):   # jest to zmienna tylko do odzytu
        return self.__stan
    
    @stan_konta.getter
    def stan_konta(self): 
        return "Stan konta" + str(self.__stan) + "zł"

    @stan_konta.setter         # setter podaje zmieniony stan konta. dodaje lub odejmuje
    def stan_konta(self, value):
        self.__stan += value

konto = KontoBankowe()
print(konto.stan_konta)

konto.stan_konta = 50
print(konto.stan_konta)
konto.stan_konta = 100
print(konto.stan_konta)
konto.stan_konta = -150  
print(konto.stan_konta)  # wynik po dodawani i doejmowaniu daje 0
