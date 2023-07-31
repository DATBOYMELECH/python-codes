#This is a collection that is unordered and unindexed
#It is created with curly braces ( {} )
#It does not allow duplicate values

utensils = {"Fork", "Spoon", "Knife", "Knife"}
dishes = {"Bowl", "Plate", "Cup"}


dinner_table = utensils.union(dishes)
difference = utensils.difference(dishes)
print(difference)
intersection = utensils.intersection(dishes)
print(intersection)

utensils.add("Napkin")
# utensils.remove("Knife")
for utensil in utensils:
    print(utensil)
