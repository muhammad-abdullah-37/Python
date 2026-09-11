# Sets in Pyhton
set1 = {1,2,3,4,5,6,7,8,9}
print("Set = ",set1)
print("Type = ",type(set1))

# Basic and Property methods of sets 

#  len() ===> Returns the length of the set
print("Length of Set1 = ",len(set1))

# type() returns the type of the set()
print(type(set1))

# in   =====> Checks if an element exists in the set and returns True and False.
print("If element is present in the set = ", 4 in set1)
print("If element is not present in the set = ",100 in set1)
print()
print()




# Adding and Updating Elements
# add() =====> Adds an element ad the end of the list
print("Set1 before adding Element = ", set1)
set1.add(100)
print("Set1 after adding Element = ", set1)
print()
print()


# update() =====> Adds multiple elements from the list , tuple etc
print("Set1 before updation = ", set1)
set1.update([10,20,30,40])
print("Set1 after updation = ", set1)
print()
print()




# Elements removing methods

# remove()  ====> Removes the element and error if element not found
print("Set1 before = ", set1)
set1.remove(100)
print("Set1 after removing an element = ", set1)
# set1.remove(1000) // error becuase element is not found
# print(set1)
print()

# discard() ====> Removes the element and no error if element not found
print(set1)
set1.discard(40)
print(set1)
print()
set1.discard(1000) # no error because of discard method
print(set1)
print()


# pop()   ====> Removes and returns a random element
print()
set1.pop()
print(set1)
print()

# clear() ====> Removes all elements from the set
set2 = {'a', 'b', 'c', 'd', 'e'}
print("Set 2 = ", set2)
set2.clear()
print("Set 2 after clear method = ", set2)
print()



# Set operation 

set3 = {'a', 'b', 'c', 'd', 'd', 'e', 'f'}
# union method ====> Combines the elements of set 1 and set 2
union_set = set1.union(set3)
print("Union of set 1 and set 2 = ",union_set)
print()


# intersection()  ====> Returns the common elemtns of set1 and set2 only

intersection_set = set1.intersection(set3)
print("intersection of Set 1 and Set 2 = ", intersection_set)
print()


# difference()  ===> returns the elements which are present in one but not in other set 

difference_set = set1.difference(set3)
print("Difference Set = ",difference_set)
difference_set2 = set3.difference(set1)
print("Difference Set 2 = ", difference_set2)
print()
print()



# Comparision and Relation methods

# issubset()  ==> checks if all elements of set 1 present in set 2 and returns True.
subset_set = set1.issubset(set3)
print("Checking for subset = ",subset_set)
print()

# issuperset()   ====> Checks if set 1 contains all elements of set 2 and returns True.
super_set = set1.issuperset(set3)
print("Checking for Superset = ",super_set)
print()
print()



# Copying a set 

# copy() =====> Retruns a shollow copy of the set 
copied_set = set1.copy()
print("Copied set   = ",copied_set)
print("Original Set = ",set1)
copied_set.pop()
print(copied_set)
print(set1)
print()
print()


# Most common and used methods of sets

commonly_used_methods = {'add()', 'update()', 'remove()', 'discard()','union()', 'intersection()', 'difference()','issubset()', 'issuperset()'}

print("Most commonly used methods of sets = ",commonly_used_methods)
print()
print()


print("Day 5 of practicing Python done")