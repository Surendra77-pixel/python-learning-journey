
#Deleting the tuples ---------------------------------
#  we cannot delete individual elements of a tuple because tuples are immutable. However, we can delete the entire tuple using the del keyword. Here is an example:

fruit = ("apple", "banana", "cherry")
del fruit
# The   tatement is used to delete the entire tuple fruit. After the deletion, trying to access the variable fruit will result in a NameError because it is no longer defined.

#clear the tuple - we can clear the contents of a tuple by converting it to a list, clearing the list, and then converting it back to a tuple. Here is an example:
my_tuple = (1, "hello", 3.14, True)
my_list = list(my_tuple)
my_list.clear()  # type: ignore
cleared_tuple = tuple(my_list)
print(cleared_tuple) #output: () - The original tuple my_tuple is converted to a list my_list, the clear() method is called on the list to remove all its elements, and then the cleared list is converted back to a tuple cleared_tuple, resulting in an empty tuple ().   

#clear wont work on tuple because of immutability - The clear() method is a list method that removes all items from a list. Since tuples are immutable, they do not have a clear() method, and you cannot modify the contents of a tuple after it has been created. Therefore, trying to call clear() on a tuple will result in an AttributeError because the method does not exist for tuples.

