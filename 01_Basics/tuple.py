tea_types = ("Black", "Green", "Oolong")
print(tea_types)

print(tea_types[-1])

# this won't work for assigning the items
# tea_types[0] = "Lemon"
# print(tea_types)

print(len(tea_types))

more_tea = ("Herbal", "Earl Grey")
all_tea = tea_types + more_tea

print(all_tea)

if "Green" in all_tea:
    print("I have the Green Tea")

more_tea = ["Herbal", "Earl Gray", "Herbal"]
print(more_tea)

# to get the count of the item
print(more_tea.count("Herbal"))

# it will assigned the values of the tea_types more like destructuring
(black, green, Oolong) = tea_types
print(black)

# more_tea.insert(1, "pink")
# print(more_tea)