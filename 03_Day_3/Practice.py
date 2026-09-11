# Practice questions 

# Write a program to ask user to enter their three favorite movies and store them in a list
# favorite_movies = []
# user_input = input("Enter your favorite movie :- ")
# favorite_movies.append(user_input)
# user_input = input("Enter your favorite movie :- ")
# favorite_movies.append(user_input)
# user_input = input("Enter your favorite movie :- ")
# favorite_movies.append(user_input)
# print(favorite_movies)


# Write a program to check if a list contains palindrome or not
# list3 = [1,2,3,4,5]
# list2 = [1,2,3,2,1]
# copied_list = list2.copy()
# copied_list.reverse()
# print(list2)
# print(copied_list)
# if copied_list == list2:
#     print("Tuple is Palindrome")
# else:
#     print("Tuple is not Palindrome")
print()


# Write a program to find the number of studetns with grade A in the given tuple
grades = ('C', 'D', 'A', 'A', 'B', 'B', 'A')
grade = "A"
print("Number fo studetns with the grades",grade , "are =",grades.count("A"))
print()


# Store the above values in a list and sort all the elements from A to D

new_list = list(grades)
print("Original or unsorted list = ", new_list)
new_list.sort()
print("New and sorted list = ",new_list)
print()

    
# Write a Python program to find the maximum and minimum elements from a tuple of numbers.
tuple1 = (1,2,3,4,5,6,7,8,9)
print("The maximum element of the tuple = ",max(tuple1))
print("The minimum element of the tuple = ", min(tuple1))
print()


# Write a program to check if a given element exists in a tuple.Example: (10, 20, 30,40) → Check if 20 is present.
tuple2 = (10,20,30,40)
finding_elment = 10
print(finding_elment in tuple2)
print()



# Write a program to: Convert a tuple to a list. Add a new element. Convert it back to a tuple.
tuple3 = [10,20,30,40,50,60,70]
print("Tuple before conversion = ",tuple3, type(tuple3))
list1 = list(tuple3)
print("Tuple after conversion to list = ", list1,type(list1))
list1.append(100)
converted_tuple = tuple(list1)
print("Converting list into tuple = ",converted_tuple, type(converted_tuple))
print()