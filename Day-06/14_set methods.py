
#set methods -

#1.add(element)-

# The add() method is used to add a single element to a set. If the element already exists in the set, it will not be added again since sets do not allow duplicate values. Here is an example:
my_set = {"apple", "banana", "cherry"}  
my_set.add("date")
print(my_set) #output: {'apple', 'banana', 'cherry', 'date'} - The add() method adds the item "date" to the set my_set. Since sets do not allow duplicate values, if we try to add an item that already exists in the set, it will not be added again.


#2.remove(element) -

# The remove() method is used to remove a specified element from the set. If the element is not found in the set, it will raise a KeyError. Here is an example:
my_set = {"apple", "banana", "cherry"}
my_set.remove("banana")
print(my_set) #output: {'apple', 'cherry'} - The remove() method is called on the set my_set to remove the item "banana". After the removal, the set contains only "apple" and "cherry". If we try to remove an item that does not exist in the set, it will raise a KeyError. For example:


#3.discard(element) - 

# The discard() method is used to remove a specified element from the set. If the element is not found in the set, it will not raise an error and the set will remain unchanged. Here is an example:
my_set = {"apple", "banana", "cherry"}
my_set.discard("banana")
print(my_set) #output: {'apple', 'cherry'} - The discard() method is called on the set my_set to remove the item "banana". After the removal, the set contains only "apple" and "cherry". If we try to discard an item that does not exist in the set, it will not raise an error and the set will remain unchanged. For example:


#4.pop() -

# The pop() method is used to remove and return an arbitrary element from the set. Since sets are unordered, you cannot predict which element will be removed. Here is an example:
my_set = {"apple", "banana", "cherry"}
removed_item = my_set.pop()
print(removed_item) #output: 'apple' (or 'banana' or 'cherry') - The pop() method removes and returns an arbitrary item from the set my_set. Since sets are unordered, the specific item that is removed cannot be predicted, and it could be any of the items in the set. After calling pop(), the set will have one less item, but we cannot determine which item was removed just by looking at the code.


#5.clear() -

# The clear() method is used to remove all items from the set, resulting in an empty set. Here is an example:
my_set = {"apple", "banana", "cherry"}
my_set.clear()
print(my_set) #output: set() - The clear() method is called on the set my_set, which removes all items from the set. After calling clear(), the set becomes empty, and when printed, it shows as set().


#6.del statement -

# We can use the del statement to delete the entire set. Here is an example:
my_set = {"apple", "banana", "cherry"}
del my_set
print(my_set) # type: ignore #output: NameError: name 'my_set' is not defined - The del statement is used to delete the entire set my_set. After the deletion, trying to access the variable my_set will result in a NameError because it is no longer defined.

#7.union() -

# The union() method is used to return a new set that contains all the unique elements from both sets. Here is an example:
st1={"apple","banana","cherry"}
st2={"date","elderberry","fig"}
st3=st1.union(st2)
print(st3) #output: {'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig'} - The set st3 is created by taking the union of st1 and st2 using the union() method. The resulting set contains all the unique elements from both sets, and since sets do not maintain order, the output may appear in a different order than the original sets.


#8.update() -

# The update() method is used to add all the unique elements from one set to another set. Here is an example:
st1={"apple","banana","cherry"}
st2={"date","elderberry","fig"}
st1.update(st2)
print(st1) #output: {'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig'} - The update() method is called on the set st1 to add all the unique elements from st2. After the update, st1 contains all the unique elements from both sets, and since sets do not maintain order, the output may appear in a different order than the original sets. Note that st2 remains unchanged after the update operation.


#9.intersection() -

#10.difference() -

#11.isdisjoint() -

#the isdisjoint() method is used to check if two sets have no elements in common. It returns True if the sets are disjoint (i.e., they have no common elements) and False otherwise. Here is an example:
st1={"apple","banana","cherry"}
st2={"date","elderberry","fig"}
result = st1.isdisjoint(st2)
print(result) #output: True - The isdisjoint() method is called on the set st1 with st2 as an argument. Since st1 and st2 have no common elements, the method returns True, indicating that the sets are disjoint. If there were any common elements between the two sets, the method would return False.



#12.issubset() -

# The issubset() method is used to check if all elements of one set are present in another set. It returns True if the set on which the method is called is a subset of the other set, and False otherwise. Here is an example:
st1={"apple","banana"}
st2={"apple","banana","cherry"}
result = st1.issubset(st2)
print(result) #output: True - The issubset() method is called on the set st1 with st2 as an argument. Since all elements of st1 ("apple" and "banana") are present in st2, the method returns True, indicating that st1 is a subset of st2. If there were any element in st1 that was not present in st2, the method would return False.

#13.issuperset() -

# The issuperset() method is used to check if a set contains all elements of another set. It returns True if the set on which the method is called is a superset of the other set, and False otherwise. Here is an example:
st1={"apple","banana","cherry"}
st2={"apple","banana"}
result = st1.issuperset(st2)
print(result) #output: True - The issuperset() method is called on the set st1 with st2 as an argument. Since st1 contains all elements of st2 ("apple" and "banana"), the method returns True, indicating that st1 is a superset of st2. If there were any element in st2 that was not present in st1, the method would return False.

