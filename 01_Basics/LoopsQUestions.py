import time

def count_positive_number(num):
    count = 0;
    for x in num:
        if x >= 0:
            count += 1
        # print(x)
    return count;

l1 = [1, -1, 2, 3,4,6,-1, -4, -5]
# print(count_positive_number(l1))

def calculate_the_sum_even(n):
    sum = 0
    for i in range(n + 1):
        if(i % 2 == 0):
            sum += i
    return sum

# num = int(input("Enter the sum: "));

# print(calculate_the_sum_even(num))

def reverseString(s):
    reverseStr = ""
    for x in range(len(s) -1, -1, -1):
        reverseStr += s[x]
    return reverseStr

# print(reverseString("hello"))

def first_nonrepeated_char(s):
    count = 0;

    for char in s:
        if s.count(char) == 1:
            print(char, end=" ")
            break

# first_nonrepeated_char("swiss")

def factorial(num):
    fact = 1;
    while(num > 0):
        fact *= num
        num -= 1
    return fact

# print(factorial(5))

def exponential_time():
    wait_time = 1
    max_retries = 5
    attempts = 0

    while attempts < max_retries:
        print("Attempt", attempts + 1, " - wait time", wait_time)
        time.sleep(wait_time)
        wait_time *= 2
        attempts += 1

exponential_time()