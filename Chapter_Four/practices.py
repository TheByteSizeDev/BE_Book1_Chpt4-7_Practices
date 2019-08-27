#Practice-Random Numbers

# 1.Use the following code to create a list of 10 random numbers. Each number will be between 0 and 6.

import random

#Import random from python???

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6, 1))
# print(my_randoms)


#2.Then iterate a different list of numbers that are sequential from 1 to 10.

# Print a message to the console indicating whether each value of `number` is in the `my_randoms` list.

new_randoms=list()
for numbers in range (1,6):
    new_randoms.append(random.randrange(1, 6, 1))
print(new_randoms)
for number in range (1,10):
    if number in new_randoms:
        print(f"new_randoms list contains {number}"),
    else:
        print(f"new_randoms list does not contain {number}")

#Practice-Planet List

# Use append() to add Jupiter and Saturn at the end of the list.
planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")

# Use the extend() method to add another list of the last two planets in our solar system to the end of the list.

planet_list.extend(["Neptune", "Planet Nine"])

# Use insert() to add Earth, and Venus in the correct order.

planet_list.insert(1, "Earth")
planet_list.insert(1, "Venus")


# Use append() again to add Pluto to the end of the list.

planet_list.append("Pluto")

# Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.

rocky_planets= planet_list[0:4]

# Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.

planet_list.remove("Pluto")
print(planet_list)



