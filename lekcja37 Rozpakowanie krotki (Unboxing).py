a, b = (2, 5)   # krotka
print(a)
print(b)

a, b = [2, 5]   # krotka
print(a)
print(b)

x = 10
y = 20
x, y = y, x
print("x:",x)      # zamiana x na y
print("y:",y)      # zamiana y na x

start, *wszystko, koniec = (1, 2, 3, 4, 5, 6, 7 )
print(start)        # 1
print(wszystko)     # (2,3,4,5,6)
print(koniec)       # 7