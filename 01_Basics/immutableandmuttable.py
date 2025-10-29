# Immutable vs Mutable in Python
# Immutable Data Types
# Immutable objects cannot be changed after creation. Any modification creates a new object.

# Common immutable types:

# Numbers (int, float, complex)
# Strings
# Tuples
# Frozenset
# Bytes
# Mutable Data Types
# Mutable objects can be modified after creation without creating a new object.

# Common mutable types:

# Lists
# Dictionaries
# Sets
# Bytearray
# User-defined classes

# Here's a detailed example with diagrams and code:

# -------- Immutable Example (String) --------
print("--- Immutable String Example ---")
# Memory diagram:
# name1 (id:1234) → "Alice"
name1 = "Alice"
print(f"Original id: {id(name1)}")

# Creates new string object
# name1 (id:5678) → "Alice Smith"
name1 = name1 + " Smith"
print(f"New id: {id(name1)}")

# -------- Mutable Example (List) --------
print("\n--- Mutable List Example ---")
# Memory diagram:
# numbers (id:9012) → [1, 2, 3]
numbers = [1, 2, 3]
print(f"Original id: {id(numbers)}")

# Modifies same list object
# numbers (id:9012) → [1, 2, 3, 4]
numbers.append(4)
print(f"Same id after change: {id(numbers)}")

# -------- Python Data Structure Categories --------

# 1. Immutable Data Structures
immutable_examples = {
    'Numbers': [42, 3.14, 2+3j],  # int, float, complex
    'Strings': "Hello World",
    'Tuples': (1, 2, 3),
    'Frozenset': frozenset([1, 2, 3]),
    'Bytes': bytes([65, 66, 67])
}

# 2. Mutable Data Structures
mutable_examples = {
    'Lists': [1, 2, 3],
    'Dictionaries': {'a': 1, 'b': 2},
    'Sets': {1, 2, 3},
    'Bytearray': bytearray([65, 66, 67])
}

# Demonstration of mutability
print("\n--- Data Structure Examples ---")
for name, example in immutable_examples.items():
    print(f"Immutable - {name}: {example}")

for name, example in mutable_examples.items():
    print(f"Mutable - {name}: {example}")

# Key differences demonstration
tuple_example = (1, [2, 3], 4)
print("\n--- Tuple with Mutable Element ---")
print("Original tuple:", tuple_example)
# While tuple is immutable, its mutable elements can be modified
tuple_example[1].append(5)
print("After modifying internal list:", tuple_example)

# Key points to remember:

# Immutable objects:

# Create new objects when modified
# Generally more memory efficient for small objects
# Thread-safe
# Can be used as dictionary keys



# Mutable objects:

# Can be modified in-place
# More memory efficient for large objects with frequent updates
# Need careful handling in multi-threaded environments
# Cannot be used as dictionary keys
# The code above demonstrates:

# ID changes for immutable objects when modified
# ID remains same for mutable objects when modified
# Different categories of data structures
# Special case of mutable objects within immutable containers
# When you run this code, you'll see how object IDs change for immutable types but stay the same for mutable types, helping visualize the concept of mutability in Python.


x = 10
y = x
print(f"x is: {(x)} and y is {(y)}")

x = 15
print(f"x is: {(x)} and y is {(y)}")

# x == 10
# and then y == 10 == x
# when x was assign as 15, y was point at 10
# Python has inbuilt grabage collection and point by reference  occurs

# https://youtu.be/MDZ4y-GgZ8k?si=R2GQiVAjfYInfnuv

#! use Slicing to make copy and reference
list1 = [1,2,3]

# not a copy but reference
list2 = list1

list3 = [3,4,45]

# to create a copy
list4 = list3[:]


# ! Equals

n = [1,2,3]
p = n

print("checking similarities:", n == p, )
print("Checking reference similarities:", n is p, )

p = [1,2,3]

print("Checking reference similarities:", n is p, )
