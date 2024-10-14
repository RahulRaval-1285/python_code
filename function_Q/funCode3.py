#Write a function that takes a number as input and returns True if the number is prime, and False otherwise.
def primeNumberChecker(number):
    is_prime = True
    condition = True
    for i in range(2, number):  
        if number % i == 0:
            is_prime = False
            break
    return is_prime

number = int(input("enter any number"))
number_check = primeNumberChecker(number)
print("number prime ",number_check)