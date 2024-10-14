#Create a Python function that takes a list of integers and returns a new list containing only the prime numbers from the original list.
# List of integers to check for prime numbers
numbers = [7, 8, 54, 35, 34, 11, 34, 52, 5, 49]
prime_numbers = []  # List to store prime numbers

# Loop through each number in the list
for num in numbers:
    if num > 1:  # Prime numbers are greater than 1
        is_prime = True  # Assume the number is prime
        for i in range(2, num):  # Check for factors from 2 to num-1
            if num % i == 0:  # If num is divisible by any of these
                is_prime = False  # It's not a prime number
                break  # Exit the loop early
        if is_prime:  # If no divisors were found
            prime_numbers.append(num)  # Add the prime number to the list

# Print the list of prime numbers
print("Prime numbers in the list:", prime_numbers)