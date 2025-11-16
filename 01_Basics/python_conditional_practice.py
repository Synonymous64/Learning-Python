
# !Problem 1
def classifyAgeGroup(age):
    if age < 0:
        print("invalid number")
    elif age <= 13:
        print("It is a child")
    elif age > 13 and age <= 19:
        print("It is a Teenager")
    elif age >= 20 and age <=59:
        print("It is an Adult")
    elif age >= 60:
        print("It is a Senior Citizen")

# age = int(input("Please Enter you age: \n"))
# classifyAgeGroup(age)

# !Problem 2
def movie_ticket_pricing(age, day):
    pricing = 0;
    if age <= 0:
        print("Invalid data")
    elif age > 0 and age < 18:
        pricing = 8
    elif age >= 18:
        pricing = 12

    if(day == "Wednesday"):
        pricing -= 2

    print(f"You have to pay {(pricing)}")

# age = int(input("Please enter you age: \n"))
# day = str(input("Please enter your day: \n"))

# movie_ticket_pricing(age, day)

# the other way
# price = 12 if age >= 18 else 8

# !Problem 3
def determine_fruit(fruit, color):
    if(fruit == "Banana"):
        if(color == "Green"):
            print("It's Unripe")
        elif(color == "Yellow"):
            print("It's Ripe")
        elif color == "Brown":
            print("It's Overripe")
    else:
        exit()

fruit = str(input("Enter Fruit: \n"))
color = str(input("Enter the Color: \n"))
determine_fruit(fruit, color)
