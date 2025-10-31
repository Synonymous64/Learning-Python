x = 1
y = 2
z = 3

print(f"Adding: {(x + y + z)}")

# Adding Paranthesis to choose which calculation should first take place
print(f"Evaluation: {((x + y) * z)}")

# Both Values being calculated should have same datatypes

a = 2
b = 1.3

print((a + b))
print(int(a + b))
print(float(a + b))

print("Tea" + "Coffee")

# to calculate the power
# print(2 ** 3)

# print("Hello"):

# Simply outputs the string to the console
# Meant for human-readable output
# Automatically adds a newline by default
# Output: Hello
# str("Hello"):

# Converts an object to its string representation
# Returns a human-readable string
# Meant for creating readable string representations of objects
# Returns: 'Hello' (but when printed, quotes aren't shown)
# repr("Hello"):

# Returns a detailed string representation of an object
# Shows exactly how to recreate the object (including quotes)
# Meant for developers and debugging
# Returns: 'Hello' (with quotes)

repr("Hello")
str("Hello")
print("Hello")

# Let's modify your code to show the differences more clearly
x = "Hello\nWorld"  # String with newline

print("1. Using print():")
print(x)  # Shows formatted output
# Output:
# Hello
# World

print("\n2. Using str():")
print(str(x))  # Shows readable string
# Output:
# Hello
# World

print("\n3. Using repr():")
print(repr(x))  # Shows exact string representation
# Output:
# 'Hello\nWorld'  - Shows the \n explicitly

# Example with a more complex object
import datetime
date = datetime.datetime.now()

print("\nWith a datetime object:")
print("print():", date)        # 2025-10-29 12:34:56.789123
print("str():", str(date))     # 2025-10-29 12:34:56.789123
print("repr():", repr(date))   # datetime.datetime(2025, 10, 29, 12, 34, 56, 789123)


# Key differences:

# print() is a function for displaying output
# str() is for converting objects to readable string format
# repr() is for generating detailed, unambiguous representation of objects
# repr() is particularly useful for:

# Debugging
# Understanding exact object representation
# Seeing special characters that might be hidden
# Creating code that could recreate the object
# str() is useful for:

# Creating human-readable string versions of objects
# General string conversion
# Formatting output

# Complex Numbers (Iota Numbers)

p = 2 + 1j;
q = p + 1;

x = p * 2;
print(q, x)

# octal numbers
y = 0o20
print(y)

#Hexal numbers
z = 0xFF
print(z);

# Binary Numbers
y = 0b1000
print(y);

# Random Choice
import random
# Between 1 to 9 (9 Included)
x = random.randint(1, 10);
print(x)

# Random choices from the lists
list1 = [1,2,3,4,5,6,7,8,9,10,100];
x = random.choice(list1);
print(x);

# Random shuffle of a list
list2 = ["Hey", "Hello", "Caio", "Marshmello"]
print(list2);
x = random.shuffle(list2);
print(list2);
