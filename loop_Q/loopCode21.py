'''
Pascal's Triangle :
        1
      1   1
    1   2   1
  1   3   3   1
1   4   6   4   1

'''

n=5
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print((i-j),end=" ")
    print()
    
'''
solution :-

    def pascal_triangle(n):
    for i in range(n):
        # Print spaces for formatting
        for j in range(n-i-1):
            print(" ", end=" ")
        
        # Initialize the first element of the row
        num = 1
        for j in range(i+1):
            print(num, end=" ")
            # Update num to the next value in Pascal's Triangle
            num = num * (i - j) // (j + 1)
        
        print()  # Move to the next row

    n = 5
    pascal_triangle(n)

'''