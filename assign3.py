# Task 1: Counting Down with Loops
# Getting the number from the user
num1 = int(input("Enter a starting number: "))
while (num1 != 0):
    # Printing the number and decrementing until 0
    print(num1)
    num1 -= 1
print("Blast off!")

# Task 2: Multiplication Table With For Loops
# Getting the number from the user
num2 = int(input("Enter a starting number: "))
for i in range (1, 11):
    # calculate the current value and print
    val = num2 * i
    print(num2, "x", i, "=", val)

# Task 3: Finding the Factorial
# Getting the number from the user
num3 = int(input("Enter a starting number: "))
fact = 1
for i in range (1, num3+1):
    # multiply by each number from one until the input
    fact = fact * i
# Printing the results!
print("The factorial of", num3, "is", fact)

