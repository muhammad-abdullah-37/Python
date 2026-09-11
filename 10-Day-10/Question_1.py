# Given a positive integer x, the task is to print the numbers from 1 to x in the order as 1 to the power 2 , 2 to the power 2, 3 to the power 2 , 4 to the power 2 , 5 to the power 2, ... (in increasing order).
user_input = int(input("Enter a positive number :- "))
count = 1
while count ** 2  <= user_input:

    print(count ** 2)
    count += 1