
#frozen set

# A frozenset is an immutable version of a set. It is a built-in data type in Python that represents an unordered collection of unique elements, just like a regular set, but it cannot be modified after it is created. Here is how you can create and use a frozenset:

#1.creating a frozenset - you can create a frozenset using the frozenset() constructor. Here is an example: 
my_frozenset = frozenset([1, 2, 3, 4, 5])
print(my_frozenset) #output: frozenset({1, 2, 3, 4, 5}) - The frozenset my_frozenset is created by passing a list of integers to the frozenset() constructor. The resulting frozenset contains all the unique elements from the list, and since frozensets do not maintain order, the output may appear in a different order than the original list.    

#1.The frozenset is immutable - once a frozenset is created, you cannot add, remove, or modify its elements. This means that you cannot use methods like add(), remove(), or clear() on a frozenset. If you try to modify a frozenset, it will raise an AttributeError. For example:

my_frozenset = frozenset([1, 2, 3])
# my_frozenset.add(4) # This will raise an AttributeError because frozensets do not have an add() method.
# my_frozenset.remove(2) # This will raise an AttributeError because frozensets do not have a remove() method.
# my_frozenset.clear() # This will raise an AttributeError because frozensets do not have a clear() method. 


#2.frozensets can be used as keys in dictionaries or as elements of other sets - since frozensets are immutable, they can be used as keys in dictionaries or as elements of other sets. This is because they have a hash value that remains constant throughout their lifetime. Here is an example:


#3,supports set operations - frozensets support all the standard set operations such as union, intersection, difference, and symmetric difference. You can use the same methods and operators that you would use with regular sets to perform these operations on frozensets. Here is an example:
frozenset1 = frozenset([1, 2, 3])
frozenset2 = frozenset([3, 4, 5])
print(frozenset1.union(frozenset2)) #output: frozenset({1, 2, 3, 4, 5}) - The union of frozenset1 and frozenset2 is calculated using the union() method, resulting in a new frozenset that contains all the unique elements from both frozensets, which are 1, 2, 3, 4, and 5. Since frozensets do not maintain order, the output may appear in a different order than the original frozensets. Note that frozenset1 and frozenset2 remain unchanged after the operation.

#4.frozensets are hashable - since frozensets are immutable, they are hashable, which means they can be used as keys in dictionaries or as elements of other sets. This is because they have a hash value that remains constant throughout their lifetime. Here is an example:
my_dict = {frozenset([1, 2, 3]): "This is a frozenset key"}
print(my_dict) #output: {frozenset({1, 2, 3}): 'This is a frozenset key'} - The dictionary my_dict is created with a frozenset as a key. The frozenset([1, 2, 3]) is used as a key in the dictionary, and it maps to the value "This is a frozenset key". Since frozensets are immutable and hashable, they can be used as keys in dictionaries without any issues. When printed, the dictionary shows the frozenset key and its corresponding value.


#frozenset methods ------------------------------------------

#  frozensets support all the standard set methods that do not modify the set, such as union(), intersection(), difference(), and symmetric_difference(). However, they do not support methods that would modify the set, such as add(), remove(), or clear(). Here is an example of using some of the supported methods:

frozenset1 = frozenset([1, 2, 3])
frozenset2 = frozenset([3, 4, 5])
print(frozenset1.intersection(frozenset2)) #output: frozenset({3}) - The intersection of frozenset1 and frozenset2 is calculated using the intersection() method, resulting in a new frozenset that contains only the elements that are present in both frozensets, which is 3. Since frozensets do not maintain order, the output may appear in a different order than the original frozensets. Note that frozenset1 and frozenset2 remain unchanged after the operation.

#copying a frozenset - 

# since frozensets are immutable, you can simply assign a frozenset to a new variable to create a copy of it. Here is an example:
frozenset1 = frozenset([1, 2, 3])
cp=frozenset1.copy()
print(cp) #output: frozenset({1, 2, 3}) - The copy() method is called on frozenset1 to create a new frozenset cp that is a copy of frozenset1. Since frozensets are immutable, the copy is essentially the same as the original, and both cp and frozenset1 will contain the same elements. When printed, cp shows the same frozenset as frozenset1.


#difference() method -

# The difference() method returns a new frozenset that contains the elements that are present in the first frozenset but not in the second frozenset. Here is an example:
frozenset1 = frozenset([1, 2, 3])
frozenset2 = frozenset([3, 4, 5])
print(frozenset1.difference(frozenset2)) #output: frozenset({1, 2}) - The difference of frozenset1 and frozenset2 is calculated using the difference() method, resulting in a new frozenset that contains only the elements that are present in frozenset1 but not in frozenset2, which are 1 and 2. Since frozensets do not maintain order, the output may appear in a different order than the original frozensets. Note that frozenset1 and frozenset2 remain unchanged after the operation.


#intersection() method -

# The intersection() method returns a new frozenset that contains only the elements that are present in both frozensets. Here is an example:
frozenset1 = frozenset([1, 2, 3])
frozenset2 = frozenset([3, 4, 5])
print(frozenset1.intersection(frozenset2)) #output: frozenset({3}) - The intersection of frozenset1 and frozenset2 is calculated using the intersection() method, resulting in a new frozenset that contains only the elements that are present in both frozensets, which is 3. Since frozensets do not maintain order, the output may appear in a different order than the original frozensets. Note that frozenset1 and frozenset2 remain unchanged after the operation.



