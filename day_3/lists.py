# A list is used to store multiple items in a single variable, it is changeabele
# Melech = [ "Melech", 13, "Melech38@gmail.com", True , 60.61]
# print(Melech[0])
# print(Melech[4])
foods = ["Pizza", "hamburger", "pudding", "spaghetti"]
foods.append("Shushi")
foods.insert(2, "ice cream")
# foods.remove("pudding")
# foods.pop()
# foods.sort(reverse=True)
# foods.clear()
# print(food)
# for food in foods:
#     print(food)
foods[0] = 'pudding'
print(foods)

squares = 1, 9, 16, 25, 36, 49, 64, 81, 100
for square in squares:
    print(square)