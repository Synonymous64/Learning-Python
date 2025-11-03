# String in PYTHON

chai = "Lemon Chai"
print(chai)
first_char = chai[0];
print(first_char)

slice_chai = chai[0:5];
print(slice_chai)

num_list = "0123456789"
print(num_list)

print(num_list[:7])
# it will create a number hoping, means it will skip the number by 2-1, it will go till 7
print(num_list[0:7:2])

# it will create a number hoping, means it will skip the number by 3-1, it will go till 7
print(num_list[0:7:3])

# lower case
print(chai.lower())
# Upper case
print(chai.upper())

# remove forward and backward trailing spaces
chai = "    Hello Chai!    "
print(chai.strip())

# Repace the char
print(chai.replace("Hello", "Greetings"));

# converting to other datatype like list
chai = " Lemon, Ginger, Masala, Mint, Mint"
# it will convert on the basis of spaces
print(chai.split())

# it will convert on the basis of comma and then after space, which will not be included
print(chai.split(", "))

# to find the by character
print(chai.find("Mint"))

# to find the count of any string
print(chai.count("Mint"));


# Formatting string with order keywords
chai_type = "Masala"
quantity = 2

order = "I would like the order {} cups of {} Chai.";
print(order.format(quantity, chai_type))

# Converting list to string
chai_variety = ["Lemon", "Masala", "Ginger", "Mint"]

print(" ".join(chai_variety))

# to find length
print(len(chai_variety))

for letter in chai:
    print(letter)

# double quote confusion
sayings = "He said, \"Faster and the furious is epic\" "
print(sayings)

# to treat a string as a raw string and print the special charaters like "\n"
chai = "Masala\nchai"
print(chai)
# r will the treat the string as raw string
chai = r"Masala\nChai"
print(chai)

# using forward slashes as well (for command line)
path = r"c:\\user\\pwd"

# using forward slashes as well (through VS code works)
path = r"c:\user\pwd"

print(path)