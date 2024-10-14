'''
*
* *
* * *
* * * *
* * * * *

'''
# Get the number of rows from the user
n = int(input("Enter the number of rows: "))

# Loop through each row
for i in range(1, n + 1):
    # Loop to print asterisks for the current row
    for j in range(1, i + 1):
        print("*", end=" ")  # Print asterisk followed by a space
    print()  # Move to the next line after printing all asterisks in the current row
