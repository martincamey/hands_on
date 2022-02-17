from animal import Animal


animal_1 = Animal("Nana", "British Shorthair", "miaulement", 4, 5)
print(animal_1.description())

animal_2 = Animal("Yunus", "Baleine Bleue", "chant", 0, 150000)
print(animal_2.description())

animal_1.mise_a_jour_poids(5.15)
print(animal_1.description())
