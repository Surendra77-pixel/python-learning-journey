
#removing the items from the set - 

# we can remove items from a set using the remove() method, discard() method, or pop()  clear  and delete method. Here are examples of each method:

#1.remove() method -
# The remove() method removes a specified item from the set. If the item is not found in the set, it raises a KeyError. Here is an example:
my_set = {"apple", "banana", "cherry"}
my_set.remove("banana")
print(my_set) #output: {'apple', 'cherry'} - The remove() method is called on the set my_set to remove the item "banana". After the removal, the set contains only "apple" and "cherry". If we try to remove an item that does not exist in the set, it will raise a KeyError. For example:
# my_set.remove("grape") # This will raise a KeyError because "grape" is not in the set my_set.

#2.discard() method - T
 
# he discard() method also removes a specified item from the set, but it does not raise an error if the item is not found. Here is an example:
my_set = {"apple", "banana", "cherry"}
my_set.discard("banana")
print(my_set) #output: {'apple', 'cherry'} - The discard() method is called on the set my_set to remove the item "banana". After the removal, the set contains only "apple" and "cherry". If we try to discard an item that does not exist in the set, it will not raise an error and the set will remain unchanged. For example:
my_set.discard("grape") # This will not raise an error because "grape" is not in the set my_set, and the set will remain unchanged.

#3.pop() method - 

# The pop() method removes and returns an arbitrary item from the set. Since sets are unordered, you cannot predict which item will be removed. Here is an example:
my_set = {"apple", "banana", "cherry"}
removed_item = my_set.pop()
print(removed_item) #output: 'apple' (or 'banana' or 'cherry') - The pop() method removes and returns an arbitrary item from the set my_set. Since sets are unordered, the specific item that is removed cannot be predicted, and it could be any of the items in the set. After calling pop(), the set will have one less item, but we cannot determine which item was removed just by looking at the code.

#if we insert the pop(1) it will give an error because pop() method does not take any arguments. The pop() method is designed to remove and return an arbitrary item from the set without specifying which item to remove. If you try to pass an argument to pop(), it will raise a TypeError because the method does not expect any parameters. For example:
# my_set.pop(1) # This will raise a TypeError because the pop() method does not take any arguments.

#4.clear() method - 

# The clear() method removes all items from the set, resulting in an empty set. Here is an example:
my_set = {"apple", "banana", "cherry"}
my_set.clear()
print(my_set) #output: set() - The clear() method is called on the set my_set, which removes all items from the set. After calling clear(), the set becomes empty, and when printed, it shows as set().


#5.del statement - 

# we can use the del statement to delete the entire set. Here is an example:
my_set = {"apple", "banana", "cherry"}
del my_set
print(my_set) # type: ignore #output: NameError: name 'my_set' is not defined - The del statement is used to delete the entire set my_set. After the deletion, trying to access the variable my_set will result in a NameError because it is no longer defined.


#learing items from the set - 

# we can clear the contents of a set using the clear() method. Here is an example:
my_set = {"apple", "banana", "cherry"}
my_set.clear()
print(my_set) #output: set() - The clear() method is called on the set my_set, which removes all items from the set. After calling clear(), the set becomes empty, and when printed, it shows as set().