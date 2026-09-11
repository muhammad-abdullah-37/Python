# # Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.

# Return True for the following cases:
# Either a or b (not both) is non-negative and the flag is false.
# Both a and b are negative and the flag is true.

# Otherwise, return False.

variable_1 = int(input("Enter your first number :- "))
variable_2 = int(input("Enter your second number :- "))
boolean_varaible = bool(input("Enter a boolean value : True or False :- "))


if variable_1 >= 0 and variable_2 < 0  or variable_1 >= 0 and variable_2 < 0 and boolean_varaible == False :
    print("True1")
elif variable_1 and variable_2 < 0 and boolean_varaible == True :
    print("True2")
else:
    print("Flase")
    