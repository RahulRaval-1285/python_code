# Write a Python program to find the factorial of a given number using a loop.
number = int(input("Enter number: "))
answer = 1

# Corrected the condition to `number > 0`
while number > 0:
    answer = answer * number
    number -= 1  # Decrease number by 1 in each iteration

print(f"Factorial of the given number is: {answer}")
