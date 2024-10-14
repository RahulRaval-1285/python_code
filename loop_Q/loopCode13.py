'''
      *
     * *
    * * *
   * * * *
  * * * * *

'''
n = 5
for i in range(1, n + 1):
    # Print leading spaces
    for j in range(n - i):
        print(" ", end="")
    
    # Print asterisks with a space after each one
    for j in range(i):
        print("*", end=" ")
    
    # Move to the next line
    print()

'''n=5
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end="   ")
    print()'''