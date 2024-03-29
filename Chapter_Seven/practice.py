#Practice-Showroom & Junkyard


# 1. Create an empty set named showroom.

showroom = set()

# 2. Add four of your favorite car model names to the set.

showroom = {'Jeep Wrangler', 'Dodge Charger', 'Ford Escape', 'Ford Mustang'}

# 3. Print the length of your set.

print(len(showroom))

# 4. Pick one of the items in your show room and add it to the set again.

showroom.add('Ford Mustang')

# 5. Print your showroom. Notice how there's still only one instance of that model in there.

# print(showroom)

# 6. Using update(), add two more car models to your showroom with another set.

new_cars = {'Honda Accord', 'Jeep Cherokee'}
showroom.update(new_cars)
print(showroom)

# 7. You've sold one of your cars. Remove it from the set with the discard() method.

showroom.discard('Ford Mustang')


#Practice- Acquiring New Cars


# Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.

junkyard = set()
junkyard = {'Ford Mustang', 'Jeep Wrangler', 'Ford Escape', 'Honda Civic'}

# Use the intersection method to see which cars exist in both the showroom and that junkyard.

print(showroom.intersection(showroom, junkyard))


# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.

new_showroom = showroom.union(junkyard)


# Use the discard() method to remove any cars that you acquired from the junkyard that you do not want in your showroom.

new_showroom.discard('Ford Mustang')


