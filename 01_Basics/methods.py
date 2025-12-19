import math
def squareOfNumber(n):
    return n ** 2

# print(squareOfNumber(3))

def Multiply(x, y):
    return x * y

# print(Multiply(3, 4))

def circleStats(radius):
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius

    return round(area, 2), round(circumference, 2);

# print(circleStats(5))

def greet(name = "User"):
    return "Hello, " + name + "!"

# print(greet("Prajwal"))
# normal function
def add(a, b):
    return a + b

# Lambda Function // if you have to use function not more than once, and storing the value in cube as, it does not have any function
cube = lambda x: x ** 3
# print(cube(3))

# using *args, to calculate all the parameter in the methods, in the same operation
def sumAll( *args):
    return sum(args)

# print(sumAll(1,2,3,4))

# kwargs
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# print_kwargs(name="Prajwal", power ="Invisible")
# print_kwargs(name = "Jack")
# print_kwargs(power = "Stealth")
# print_kwargs(power = "Stealth", enemy = "Dr. Doom")
# print_kwargs(power = "Stealth", enemy = 1)

def even_generator(limit):
    li = []
    for i in range(2, limit + 1, 2):
        yield i


print(even_generator(10))