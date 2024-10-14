#Create a Python program that reads a list of integers and returns the sum of all elements at even indices (0, 2, 4, etc.).
numbers = [6,7,8,4,3,6,36,2,4,56]
sum = 0
for num in numbers :
    if numbers.index(num) % 2 ==0 :
        sum += num
print("sum of even index is : ",sum)
'''
# Create a Python program that reads a list of integers and returns the sum of all elements at even indices (0, 2, 4, etc.)
numbers = [6, 7, 8, 4, 3, 6, 36, 2, 4, 56]
sum = 0

# Using enumerate to get both index and value
for index, num in enumerate(numbers):
    # Check if the index is even
    if index % 2 == 0:
        sum += num

print("Sum of elements at even indices is:", sum)
'''