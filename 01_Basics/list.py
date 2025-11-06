tea_varities = ["Black", "Green", "Oolong", "White"]
print(tea_varities)

print(tea_varities[(len(tea_varities) - 1)])

print(tea_varities[:2])

tea_varities[3] = "Herbal"

print(tea_varities)

print(tea_varities[1:2])
# adding values in such manner will add Lemon in the form of array
# tea_varities[1:2] =  "Lemon"
print(tea_varities)
# this is the correct manner
tea_varities[1:2] = ["Lemon"]
print(tea_varities)

tea_varities[1:3] = ["Masala", "Green"]
print(tea_varities)

# to add different elements
tea_varities.append("Cinnamon")
print(tea_varities)

# it will give the output as empty array
print(tea_varities[1:1])

# but it will add the elements in the specific position, as we are not returning anything
tea_varities[1:1] = ["test1", "test2"]
print(tea_varities);

print(tea_varities[1:2])

# passing the empty array is equivalent of deleting the specific element of the array
tea_varities[1:3] = []

print(tea_varities)

for tea in tea_varities:
    print(tea, end=" ")


for tea in tea_varities:
    if(tea == "Cinnamon"):
        print(f"this is {(tea)}", end=" ")
    else:
        print(f"{(tea)} is not cinnamon")
print()


# for tea in tea_varities:
#     if(tea == "Cinnamon"):
#         print(f"this is {(tea)}")

# other way

if "Green" in tea_varities:
    print("I have Green tea")

# to delete the element from the list and it gives the final value, deletes the last element
deleteMe = tea_varities.pop();
print(deleteMe)
print(tea_varities)


# remove element can delete specific element named
p = tea_varities.remove("Green");
# but it doesn't return back the deleted element like in the case of pop
print(p);

print(tea_varities)

# to add the element in the specific position, we have to give the index and element name
tea_varities.insert(1, "Green");
print(tea_varities)

# making a copy using slicing
tea_varities_copy = tea_varities[:]
# or use can use the copy function
tea_varities_copy = tea_varities.copy()
print(tea_varities_copy)


# using loop inside the range
square_num = [3 * x  for x in range(2, 10)]
print(square_num)

cube = [x ** 3 for x in range(1, 11)]
print(cube)

