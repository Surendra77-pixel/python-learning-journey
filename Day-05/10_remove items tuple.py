
#1.removing the items in the tuple -

#  since tuples are immutable, we cannot remove individual items from a tuple. However, we can create a new tuple that excludes the item we want to remove. Here is an example: 

my_tuple = (1, "hello", 3.14, True)
item_to_remove = "hello"
new_tuple = tuple(item for item in my_tuple if item != item_to_remove)
print(new_tuple) #output: (1, 3.14, True) - The new_tuple is created by using a generator expression that iterates through each item in the original tuple my_tuple and includes only those items that are not equal to the item_to_remove ("hello"). As a result, the new_tuple contains all the elements of my_tuple except for "hello", resulting in (1, 3.14, True).

#2.del statement - we can use the del statement to delete the entire tuple. Here is an example:
my_tuple = (1, "hello", 3.14, True)
del my_tuple
print(my_tuple) # type: ignore #output: NameError: name 'my_tuple' is not defined - The del statement is used to delete the entire tuple my_tuple. After the deletion, trying to access the variable my_tuple will result in a NameError because it is no longer defined.  

# The del statement is used to delete the entire tuple my_tuple. After the deletion, trying to access the variable my_tuple will result in a NameError because it is no longer defined.


#3.There is an other method to remove items from a tuple by converting it to a list, removing the item, and then converting it back to a tuple. Here is an example:

Thistuple=("apple","banana","cherry" )
y=list(Thistuple)
y.remove("banana")
Thistuple=tuple(y)
print(Thistuple) #output: ('apple', 'cherry') - In this example, we first convert the tuple Thistuple to a list y. Then we use the remove() method to remove the item "banana" from the list. Finally, we convert the list back to a tuple and assign it to Thistuple. The resulting tuple contains only "apple" and "cherry".

