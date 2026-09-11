# lists in python
list1= [1,2,9,4,8,6,7,5,3]
print(type(list1))

# list methods

# append() ====> adds one element at the end
list1.append(1000)
print(list1)
print()

# sort() ====> sorts the lists in ascending order
list1.sort()
print("Sorted list in ascending order = ",list1)
print()

# sorting in descending order
list1.sort(reverse=True)
print("List sorted in Descending order = ",list1)
print()

# insert(element, index) ====> adds an element at a particular index
list1.insert(3, 100)
print(list1)
print()


# remove(element) ===> removes the first occurence of the element
list1.remove(1000)
print(list1)
print()


# pop(index) removes an element at a particular index
list1.pop(2)
print(list1)
# list1.pop(100) if that index is not present or out of index then it return indexerror
# print(list1)
print()