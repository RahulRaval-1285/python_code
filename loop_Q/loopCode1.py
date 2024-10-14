#Write a Python program using a for loop that iterates through a list of numbers and prints only the even numbers.

numbers = [1,3,2,5,585,54,68,15,6541,54,454,85]
for num in numbers :
    if num % 2 == 0 :
        print(f"{num} is a even")
    else :
        print(f"{num} is odd")