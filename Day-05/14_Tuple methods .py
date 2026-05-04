
#The tuple methods -----------------------------

#The tuple data type has several built-in methods that allow us to perform various operations on tuples. Here are some of the commonly used tuple methods:

#1.count() -
 
# The count() method is used to count the number of occurrences of a specified value in a tuple. It takes one argument, which is the value to be counted, and returns the number of times that value appears in the tuple. Here is an example:
my_tuple = (1, 2, 3, 2, 4, 2)
print(my_tuple.count(2)) #output: 3 - The count() method is called on the tuple my_tuple with the argument 2. It counts the number of times the value 2 appears in the tuple, which is 3, and returns that count.   



#2.index() -

#  The index() method is used to find the index of the first occurrence of a specified value in a tuple. It takes one argument, which is the value to be searched for, and returns the index of the first occurrence of that value in the tuple. If the value is not found, it raises a ValueError. Here is an example:
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple.index(3)) #output: 2 - The index() method is called on the tuple my_tuple with the argument 3. It searches for the value 3 in the tuple and returns the index of its first occurrence, which is 2 (since indexing starts at 0). If we were to search for a value that is not in the tuple, such as 6, it would raise a ValueError.


#3.tuple() constructor -

# The tuple() constructor is used to create a new tuple from an iterable (like a list, string, or another tuple). It takes an iterable as an argument and returns a new tuple containing the elements of that iterable. Here is an example:
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple) #output: (1, 2, 3, 4, 5) - The tuple() constructor is called with the list my_list as an argument. It converts the list into a tuple, resulting in the new tuple (1, 2, 3, 4, 5). The elements of the original list are now contained within the new tuple.


#4.len() function -

# The len() function is used to get the number of items in a tuple. It takes a tuple as an argument and returns the length of that tuple. Here is an example:
my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple)) #output: 5 - The len() function is called with the tuple my_tuple as an argument. It calculates the number of items in the tuple, which is 5, and returns that value. The output indicates that there are 5 elements in the tuple.


