#Write a function that takes a list of numbers as input and returns the largest number in the list.
def maxNumberfinder(numbers):
    maxNumber = numbers[0]
    for num in numbers :
        if num > maxNumber:
            maxNumber = num
    return maxNumber
numbers = [1,2,3,4,5,6,7,8,9,10]
number = maxNumberfinder(numbers)
print("max number is ",number)