# Question: Write a Python program that iterates through a list of strings and counts how many of those strings have a length greater than 5 characters. Finally, print the count.
Strings = ["hgiufh","rahul","levi","mindset","silicon","abc"]
count = 0
for word in Strings :
    if len(word) > 5 :
        count += 1
print(f"there are total {count} words who have more then 5 charter")