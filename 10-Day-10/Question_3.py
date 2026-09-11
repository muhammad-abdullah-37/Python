# Given two numbers a and b; you need to perform basic mathematical operation on them. You will be provided an integer named as operator. 
# If operator equals to 1 add a and b, then print the result 
# If operator equals to 2 subtract b from a, then print the result 
# If operator equals to 3 multiply a and b, then print the result 
# If operator equals to any another number, print "Invalid Input"(without quotes).


first_number = int(input("Enter your first number:- "))
second_number = int(input("Enter your second number:- "))
operand = int(input("Enter 1 for adding, 2 for substration, 3 for multiplication:- "))
if operand == 1 :
    print(first_number, "+", second_number, "=",first_number + second_number)
elif operand == 2 :
    print(first_number, "-", second_number, "=",second_number - first_number)
elif operand == 3 : 
    print(first_number, "*", second_number, "=",first_number * second_number)
else :
    print("Invalid Operator")