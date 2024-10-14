# List of numbers
numbers = [46, 4165, 46, 15, 5, 7, 845, 4, 1, 8]

# Initializing min and max
min_value = numbers[0]  # Set to the first element
max_value = numbers[0]  # Set to the first element

# Iterating through the list
for num in numbers:
    if num < min_value:
        min_value = num  # Update min if current number is smaller
    if num > max_value:
        max_value = num  # Update max if current number is larger

# Printing the results
print(f"Max number is {max_value} and Min number is {min_value}")
