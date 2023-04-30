animals = ["Kot", "Pies", "Koń", "Krowa", "Lis", "Dzik", "Kret", "Bober"]
for animal in enumerate(animals):
    print(animal)

animals = ["Kot", "Pies", "Koń", "Krowa", "Lis", "Dzik", "Kret", "Bober"]
for index, animal in enumerate(animals):
    print(animal)

animals = ["Kot", "Pies", "Koń", "Krowa", "Lis", "Dzik", "Kret", "Bober"]
for index, animal in enumerate(animals):
    print(index, animal)

animals = ["Kot", "Pies", "Koń", "Krowa", "Lis", "Dzik", "Kret", "Bober"]
for index, animal in enumerate(animals):
    if index % 2 == 0:
        continue
    print(index, animal)

animals = ["Kot", "Pies", "Koń", "Krowa", "Lis", "Dzik", "Kret", "Bober"]
for index, animal in enumerate(animals):
    print(f"{index+1}.\t{animal}")
