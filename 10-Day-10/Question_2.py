# Given a number n, print the multiplication table from 1 to 10 for n in a single line, separated by spaces.

user_input = int(input("Enter your number to print its table :- "))
for index in range(1,user_input):
    print(user_input, "*", index, "=", user_input * index)
