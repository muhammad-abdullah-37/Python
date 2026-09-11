# String Methods or functions
user_name = "Ali"
print("Length of " , user_name, "=",len(user_name))
print()
# lower() method
print(user_name.lower())
print()

# upper() methos
print(user_name.upper())
print()

# Capitalize method
print(user_name.capitalize())
print()

# strip method
user_name = "    Ali "
print("Without the strip method = ",user_name)
print("With the strip method = ",user_name.strip())




string_1 = "Hello today is the day 2 of the learning Python"

# replace() method
print(string_1.replace("2", "two"))
print()

# endswith() method for checking the string ends with that word or not
print(string_1.endswith("school"))
print(string_1.endswith("Python"))
print()

# finds() method for finding a word or character in a string
print(string_1.find("the"))
print()

# count() counts how many times a substring is present
print(string_1.count("a"))
print(string_1.count("the"))
print("If the given substring is not present it returns ",string_1.count("college"))
print()

# startswith() checks if a string is started with a character or not
print("If it does not starts with the substring then it returns = ",string_1.startswith("hi"))
print("If it  starts with the substring then it returns = ",string_1.startswith("Hello"))
print()

# endswith() checks if a string ends with the given substring or not
print("If it does not ends with the substring then it returns = ",string_1.endswith("python"))
print("If it ends with the substring then it returns = ",string_1.endswith("Python"))
print()


# title() Capitalize the first letter of each word
print(string_1.title())
print()

# isalnum() checks if all the characters are alphanumeric
print("Checking if all the characters are alphanumeric or not , , if not then it returns = ",string_1.isalnum())
print()


# isalpha() checking if all the characters are alphatic
print("Checking if all the characters are alphabets or not , , if not then it returns = ",string_1.isalpha())
print(string_1)