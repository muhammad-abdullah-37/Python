# Loops is Python

str1 = "Hello World"
for c in str1:
    print(c)
    
    
    
# Write a while loop that prints the numbers from  1 to 100
number = 1
while number <= 100:
    print(number)
    number += 1
    
    
# Write a program that print Numbers 1 to 10 Use a while loop to print numbers from 1 to 10.
number2 = 0 
while number2 <= 10:
    print(number2)
    number2 += 1
    
    
# Countdown Use a while loop to print numbers from 10 down to 1.
number3 = 10
while number3 >= 1:
    print(number3)
    number3 -= 1


# Write a program that print Digits of a Number. Take an  input (like 1234) and use a while loop to print each digit separately.

user_input = list (input("Enter your number :- "))
index = 0
while index < len(user_input) :
    print(user_input[index])
    index += 1


# Write a program that Use a while loop to calculate the sum of numbers from 1 to 5.
sum = 1
index2 = 1
while index2 <= 5:
    sum = sum * index2 
    print(sum )
    index2 += 1
    
    
# Write a simple game where the user keeps guessing a number (say, 7) until they get it right. Use a while loop. 
user_number = int (input("Enter Your Number :- "))
target_number = 7
while user_number != target_number :
        user_number = int (input("Enter Your Number :- "))
print("You Guessed the number successfully = ",target_number )
    
    