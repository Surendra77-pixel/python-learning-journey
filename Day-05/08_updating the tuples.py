
#updating the tuples ---------------------------------

# 1.we cannot update individual elements of a tuple because tuples are immutable. However, we can create a new tuple by concatenating the existing tuple with another tuple that contains the updated values. Here is an example:

my_tuple = (1, "hello", 3.14, True)
new_tuple = my_tuple + (False,) 
print(new_tuple) #output: (1, 'hello', 3.14, True, False) - The new_tuple contains all the elements of the original tuple my_tuple followed by the new element False, resulting in (1, 'hello', 3.14, True, False).

#2.by changing the tuple to a list and then back to a tuple - we can convert the tuple to a list, update the list, and then convert it back to a tuple. Here is an example:

my_tuple = (1, "hello", 3.14, True)
my_list = list(my_tuple)
my_list[1] = "world"  # type: ignore
updated_tuple = tuple(my_list)
print(updated_tuple) #output: (1, 'world', 3.14, True) - The original tuple my_tuple is converted to a list my_list, the second element of the list is updated to "world", and then the updated list is converted back to a tuple updated_tuple, resulting in (1, 'world', 3.14, True).