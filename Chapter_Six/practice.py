# 1. Create a tuple named zoo that contains 10 of your favorite animals.

zoo = ("Lion", "Tiger", "Giraffe", "Red Panda", "Rhino", "Monkey", "Lemur", "Fruit Bat", "Buffalo", "Flamingos")

# 2. Find one of your animals using the tuple.index(value) syntax on the tuple.

favorite_animal = zoo.index("Fruit Bat")

# 3. Determine if an animal is in your tuple by using value in tuple syntax.

animal_to_find = "Giraffe"
if animal_to_find in zoo:
    print(f"{animal_to_find} is in our zoo")
else:
    print(f"{animal_to_find} is not in our zoo")

# 4. You can reverse engineer (unpack) a tuple into another tuple with the following syntax. Create a variable for the animals in your zoo tuple, and print them to the console.

(first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eigth_animal, ninth_animal, tenth_animal) = zoo
print(first_animal)
print(eigth_animal)

# 5. Convert your tuple into a list.

zoo_list = [first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eigth_animal, ninth_animal, tenth_animal]

# 6. Use extend() to add three more animals to your zoo.

zoo_list.extend(["Ant Eater"])
zoo_list.extend(["Tarantula"])

# 7. Convert the list back into a tuple.

zoo_t = tuple(zoo_list)