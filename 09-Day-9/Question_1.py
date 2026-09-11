# You are given a number  and you have to print your answer according to the following:
# If the number is divisible by 3, you print "Fizz" (without quotes)
# If the number is divisible by 5, you print "Buzz" (without quotes)
# If the number is divisible by both 3 and 5, you print "FizzBuzz" (without quotes)
# In any other case, you print the number itself

# Note: You should add a newline character after print() statement.

user_input = int(input("Enter a number:- "))
if user_input % 3 == 0 and user_input % 5 == 0 :
    print("FizzBuzz")
elif user_input % 3 == 0:
    print("Fizz")
elif user_input % 5 == 0 :
    print("Buzz")
else:
    print(user_input)