def dzielenie(x, y):
    assert y != 0, "Y == 0"                # dzielenie przez 0
    if y == 0:
        raise ZeroDivisionError("Dzilenie przez 0")
    print(x / y)            # wywołujemy błędy        

try:
    dzielenie(2, 0)         # dzielenie jest błedne zamien na np.4
except ZeroDivisionError:
    print("błąd")
    raise

