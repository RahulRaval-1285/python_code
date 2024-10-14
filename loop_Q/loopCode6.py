# Question: Write a Python program that iterates through a list of mixed data types (integers, strings, and floats) and creates a new list containing only the strings from the original list. Finally, print the new list.
'''list = ["sagu",70,6.6,"mooo",98,9.06]
int_list = []
string_list = []
float_list = []
for next in list :
    if type(next)=="int" :
        int_list.append(next)
    elif type(next)=="str" :
        int_list.append(next)
    elif type(next)=="float" :
        int_list.append(next)
print("integer list")
for x in int_list :
    print(x, end = ",")
print("string list")
for x in string_list :
    print(x, end = ",")
print("float list")
for x in float_list :
    print(x, end = ",")'''
# List of mixed data types
mixed_list = ["sagu", 70, 6.6, "mooo", 98, 9.06]
int_list = []
string_list = []
float_list = []

# Iterating through the mixed list
for item in mixed_list:
    if type(item) == int:  # Check if the item is an integer
        int_list.append(item)
    elif type(item) == str:  # Check if the item is a string
        string_list.append(item)  # Append to the string list
    elif type(item) == float:  # Check if the item is a float
        float_list.append(item)  # Append to the float list

# Printing the results
print("Integer list:")
for x in int_list:
    print(x, end=", ")
    
print("\nString list:")
for x in string_list:
    print(x, end=", ")

print("\nFloat list:")
for x in float_list:
    print(x, end=", ")
