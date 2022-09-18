# This is a sample Python script.
import random


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

n = int(input("enter a value"))
if n % 2 == 0:
    print("given no is even number")
else:
    print("given no is odd number")

# Activity no 2

num = int(input("enter a number"))
sum = num

while num != 0:
    num = int(input("enter a number"))
    sum += num
print("result:", sum)

# Activity no 3

num = int(input("Enter a number: "))

# define a flag variable
flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

# Activity no 4:

sum = 0
i = 0
while i <= 4:
    n = int(input("enter a value"))
    sum += n
    i = i + 1
print("sum is:", sum)

# Activity no 5

sum = 0
i = 0
while i <= 10:
    num = int(input("enter a number "))
    sum += n
    i = i + 1


print("sum is", sum)

# Activity no 6

n = input("enter your name")
print("name", n)
p = input("where are you from")
print("place", p)

# Activity no 7
MINIMUM = 1
MAXIMUM = 9
NUMBER = random.randint(MINIMUM, MAXIMUM)
GUESS = None
ANOTHER = None
TRY = 0
RUNNING = True
print("Alright...")
while RUNNING:
    GUESS = input("What is your lucky number? ")
    if int(GUESS) < NUMBER:
        print("Wrong, too low.")
    elif int(GUESS) > NUMBER:
        print("Wrong, too high.")
    elif GUESS.lower() == "exit":
        print("Better luck next time.")
    elif int(GUESS) == NUMBER:
        print("Yes, that's the one, %s." % str(NUMBER))
    if TRY < 2:
        print("Impressive, only %s tries." % str(TRY))
    elif 2 < TRY < 10:
        print("Pretty good, %s tries." % str(TRY))
else:
    print("Bad, %s tries." % str(TRY))
RUNNING = False
TRY += 1
