# Question: Write a Python program that iterates through a list of integers and creates a new list that contains only the square of each positive integer from the original list. Finally, print the new list.
# List of integers
numbers = [-1, 3, 4, 0, -5, 7, -8]
newList = []

# Iterating through the list
for num in numbers:
    if num >= 0:
        squared_num = num ** 2  # Calculate the square of the positive number
        newList.append(squared_num)  # Add the squared number to the new list

# Printing the new list
print("The squares of positive integers are:", newList)