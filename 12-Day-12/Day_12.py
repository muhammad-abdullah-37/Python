# Day 12 of Python, Practice questions related to file i/o 

# Question 1 

# Create a new file "practice.txt" using python. Add the following in it. 
# "Hi everyone 
# we are learning File i/o
# using Java
# I like programming in Java"


# Solving question using with syntax approach
with open("practice.txt", "w") as f :
    f.write("Hi everyone\nwe are learning File i/o\nusing Java\nI like programming in Java")

# Write a function that replaces all the occurance of the Java with Python
def check_for_word ():
    with open("practice.txt", "r") as f :
        data = f.read()
        print(data)
    new_data = data.replace("Java", "Python")
    print("=======================================================================")
    print(new_data)
    with open("practice.txt", "w") as f :
        f.write(new_data)
check_for_word()
    
    
    

# Search if the word "learning" exists in the file or not.
print("===============================================================================================")
targer_word = "learning"
with open("practice.txt", "r") as f :
    data = f.read()
    print("Whole data = ", data)
    if(data.find(targer_word) != -1) :
        print("Found")
    else:
        print("Not found")