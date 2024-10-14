'''
        *
      * *
    * * *
  * * * *
* * * * *

'''
n = 5
for i in range(1, n + 1):
    # Print spaces to shift the stars to the right
    for j in range(n, i, -1):
        print(" ", end=" ")

    # Print the asterisks
    for j in range(1, i + 1):
        print("*", end=" ")
    
    # Move to the next line after each row
    print()
