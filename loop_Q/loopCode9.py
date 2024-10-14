# Write a Python program that takes a list of strings and creates a new list where each string is converted to uppercase.
words = ["rahul", "sagar", "levi", "wood", "stronger"]
upperCaseList = []

# Loop through each word in the list and convert it to uppercase
for word in words:
    upperCaseList.append(word.upper())

# Print the list containing the uppercase words
print(upperCaseList)
