# Question: Write a Python program that iterates through a list of numbers and calculates the sum of only the odd numbers. Finally, print the total sum.
numbers = [34,6,45,456,344,65,34457,344,5645,54]
sum = 0
for num in numbers :
    if num % 2 != 0 :
        sum = sum + num #sum += num
        
print("sum of odd number from list is ",sum)