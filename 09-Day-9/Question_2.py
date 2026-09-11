# Question Number 2

# Given a positive integer x. Your task is to check, if it is even or odd (Any number that gives zero as remainder when divided by 2 is an even number).
# Note: Return "Even" if the number is even; otherwise, return "Odd".

user_input = int(input("Enter a number to check it is Even or Odd:- "))
if user_input % 2 == 0:
    print("Even")
else:
    print("Odd")
