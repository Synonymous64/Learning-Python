# Dictionary have keys and values
chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}

print(chai_types)

print(chai_types["Masala"])
print(chai_types.get("Masala"))

# to change th values
chai_types["Green"] = "Fresh"
print(chai_types)

# to print the key
for chai in chai_types:
    print(chai)

# to print the values
for chai in chai_types:
    print(chai, chai_types[chai])

# to access both using a loop
for key, value in chai_types.items():
    print(key, value)

if "Masala" in chai_types:
    print("I have the Masala")

# to print the len of the dictionary
print(len(chai_types))

# to add the key and element
chai_types["Eary Grey"] = "Citrus"
print(chai_types)

# to use the pop but you have to provide the key

pop = chai_types.pop("Ginger")
print(pop);
print(chai_types)

# pop item will remove the last item, it does not need any key to delete
pop = chai_types.popitem();
print(pop)
print(chai_types)

chai_types.pop("Green");
print(chai_types)

# to make the copy
chai_types_copy = chai_types.copy();
print(chai_types_copy)

tea_shop = {"chai": {"Masala": "Spicy", "Ginger": "Zesty"},
            "Tea": {"Green": "Mild", "Black": "Strong"}}

print(tea_shop)
print(len(tea_shop))

# you can also print the specific Key values
print(tea_shop["chai"])

# you can also print the specific value from the key
print(tea_shop["chai"]["Ginger"])

# doing calculations in the dictionary
squared_nums = {x: x ** 2 for x in range (1, 11)}
print(squared_nums)

keys = ["Masala", "Ginger", "Lemon"]
print(keys)

default_value = "Delicious"

# creating the dictionary using random variables
# first method
new_dict = {default_value: keys}
print(new_dict)

# second method each key with defualt value
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)

# other way
new_dict = dict.fromkeys(keys, keys)
print(new_dict)