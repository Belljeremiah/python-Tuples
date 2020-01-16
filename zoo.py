# creating a tuple like a list but immutable
zoo = ("echidna", "fennec fox", "unicorn", "deathmetal unicorn", "opossum", "water-horse", "sloth", "narwhal", "Bonnacon", "merman")

# create a variable for my animals in zoo tuple
(first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eighth_animal, ninth_animal, ninth_animal) = zoo

# use index method to find the value of one animal

zoo.index("deathmetal unicorn")

# Determine if an animal is in your tuple by using value in tuple syntax

animal_to_find = "deathmetal unicorn"
if animal_to_find in zoo:
    print(zoo)

# converting tuple (zoo) into a list and printing it after set as variable list_animals
list_animals = list(zoo)
print(list_animals)