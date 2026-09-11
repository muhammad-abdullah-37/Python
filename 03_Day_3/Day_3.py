# Tuples in Python
tuple1 = (1,2,3,4,5,6,7,8,9, 6 , 3)
print("The Type is ",type(tuple1))


# Tuples methods
# Most commonly used methods
# len() methods to check the length of the tupel
print()
print("Length of tuple = ",len(tuple1))
print()


# count() method to count how many times an element is present 
print(tuple1.count(6))
print(tuple1.count(2))
print()


# max()  gives the highest or maximum value element in a tuple
print("Maximum or highes value in the tuple = ",max(tuple1))
print()


# min() gives the lowest or minimum values
print("Minimum or lowest value in tuple = ",min(tuple1))
print()



# Searching and counting methods

# index(element) gives the index of the that element in the tuple
print("Index of the given element = ",tuple1.index(3))
print()

# count(element) returns how many tinmes an element is present in the tuple
print(tuple1.count(9))
print(tuple1.count(3))
print()

# in  in in tuples
print("Checking if the element in tuple is present it returns = ",4 in tuple1)
print("Checking if the element in tuple is not present in then it returns = ",10 in tuple1)
print()



# Mathematical methods of tuples
# sum(tuple) Returns the sum of all elements of the tuple
print("Sum of all elements in the tuple = ",sum(tuple1))
print()

# max(tuple) Returns the largest or highest element in the tuple
print("Maximum element in the tuple =",max(tuple1))
print()



# Sorting and Ordering Methods
# sorted() sorts the elements in an ascending order
print("Unsorted tuple = ", tuple1)
print("Sorted tuple =",sorted(tuple1))
print()
