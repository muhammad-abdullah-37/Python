# You are given a String S, you need to print its characters at even indices(index starts at 0).

user_input = input("Enter a your name:- ")
idx = 0
for character in user_input:
    if idx % 2 == 0:
        print(character)
    idx += 1