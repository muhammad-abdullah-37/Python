# File I/O in Python
# I/O Syntax in Python

# Reading file
file_1 = open("demo.txt", "r")
print(file_1.read())


# Reading the specific or limited number of characters 
file_2 = open("demo.txt", "r")
print(file_2.read(7))

# Reading the file line by line
# First line 
line_1 = file_2.readline()
print("First Line in Demo File = ",line_1)

# Reading 2nd line in a file
second_line = file_2.readline()
print("Second Line ====== ", second_line)
file_1.close()
file_2.close()

#  Write operation 
file_2 = open("demo.txt", "w")
file_2.write("I am updating the Python file and erasing all the previous text.")
file_2.close()


file_2 = open("demo.txt", "w")
file_2.write("Hello , I am learning file i/o in python and it seems very intersting.")

# updation using append instead of write operation

file_2 = open("demo.txt", "a")
file_2.write("\n After that I will move to the OOPS in Python and then I will learn Djnago")

# r+ , a+ and w+ operations


# r+ operator is used for reading and writing the file. It positioned the pointer in the beginning and starts replacoing the characters from the beginning
file_2 = open("demo.txt", "r+")
file_2.write("I am using r+ operator")


# w+ operator is used for opening and reading the file, it trancats the file and rewrite the file.
file_2 = open("demo.txt", "w+")
file_2.write("I am using the w+ opertor while learning file I/O in Python.")


# a+ is used for reading and writing the file , The pointer is positioned at the end , it only updates the file by adding the new content at the end without removing the previous content
file_2 = open("demo.txt", "a+")
file_2.write("I am using the Append + operation")



# Using operation with "With" sytax

with open("demo.txt", "r") as f :
    data = f.read()
    print("Sample file data : ", data)
    

with open("demo.txt", "w") as f :
    f.write("I am writing the demo file using the write opration with the help of 'with' sytanx")
    


import os 
os.remove("sample.txt")
