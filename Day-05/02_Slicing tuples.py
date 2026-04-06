
#slicing tuples------------------------------

#1.slicing a tuple - 

# we can slice a tuple to create a new tuple that contains a subset of the original elements. The syntax for slicing a tuple is similar to slicing a list, where you specify the start index, end index, and step (optional) in the format tuple[start:end:step]. Here is an example:

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4]) #output: (2, 3, 4) - The slicing my_tuple[1:4] creates a new tuple that contains the elements from index 1 to index 3 (4 is excluded) of the original tuple my_tuple, resulting in (2, 3, 4).

#2 slicing with negative indices - 

# we can also use negative indices in slicing to specify the start and end positions from the end of the tuple. Here is an example:

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[-4:-1]) #output: (2, 3, 4) - The slicing my_tuple[-4:-1] creates a new tuple that contains the elements from index -4 to index -2 (index -1 is excluded) of the original tuple my_tuple, resulting in (2, 3, 4).


#3.slicing with step - 
# we can also specify a step value in the slicing syntax to skip elements in the original tuple. Here is an example:
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0:5:2]) #output: (1, 3, 5) - The slicing my_tuple[0:5:2] creates a new tuple that contains the elements from index 0 to index 4 (5 is excluded) of the original tuple my_tuple, but only includes every second element (step of 2), resulting in (1, 3, 5).

#4.slicing with negative step - 
# we can also use a negative step value to slice a tuple in reverse order. Here is an example:
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[4:0:-1]) #output: (5, 4, 3, 2) - The slicing my_tuple[4:0:-1] creates a new tuple that contains the elements from index 4 to index 1 (0 is excluded) of the original tuple my_tuple, but in reverse order (step of -1), resulting in (5, 4, 3, 2).

#5.slicing with negative indices -
#  we can also use negative indices in slicing to specify the start and end positions from the end of the tuple. Here is an example:
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[-1:-6:-1]) #output: (5, 4, 3, 2, 1) - The slicing my_tuple[-1:-6:-1] creates a new tuple that contains the elements from index -1 to index -5 (index -6 is excluded) of the original tuple my_tuple, but in reverse order (step of -1), resulting in (5, 4, 3, 2, 1).here the index 6 is excluded because the slicing stops before reaching index -6, which is the stopping point for the slice. The slice includes elements from index -1 to index -5, but does not include the element at index -6 and we have to rembwe that the -6 is not presnt in the list befor the slicing because the slicing stops before reaching index -6, which is the stopping point for the slice. The slice includes elements from index -1 to index -5, but does not include the element at index -6.


#6.slicing with step and negative indices - 
# we can also combine the use of step and negative indices in slicing to create more complex slices. Here is an example:
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[-1:-6:-2]) #output: (5, 3, 1) - The slicing my_tuple[-1:-6:-2] creates a new tuple that contains the elements from index -1 to index -5 (index -6 is excluded) of the original tuple my_tuple, but only includes every second element (step of -2) in reverse order, resulting in (5, 3, 1).


#7.revesring a tuple - 
# we can reverse a tuple using slicing with a step of -1. Here is an example:
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[::-1]) #output: (5, 4, 3, 2, 1) - The slicing my_tuple[::-1] creates a new tuple that contains all the elements of the original tuple my_tuple but in reverse order (step of -1), resulting in (5, 4, 3, 2, 1).


a = (1, 2, 3, 4, 5, 6)
print(a[::2]) #output: (1, 3, 5) - The slicing a[::2] creates a new tuple that includes every second element from the original tuple a. In this case, it starts from the first element (index 0) and includes every second element, resulting in the output (1, 3, 5).

a = (1, 2, 3, 4, 5)
print(a[::-2]) #output: (5, 3, 1) - The slicing a[::-2] creates a new tuple that includes every second element from the original tuple a but in reverse order. In this case, it starts from the last element (index -1) and includes every second element in reverse order, resulting in the output (5, 3, 1).  can be used to reverse a tuple and skip elements at the same time.

a = (1, 2, 3, 4, 5)
print(a[1::2]) #output: (2, 4) - The slicing a[1::2] creates a new tuple that includes every second element from the original tuple a, starting from index 1. In this case, it includes the elements at index 1 and index 3, resulting in the output (2, 4).

a = (1, 2, 3, 4, 5)
print(a[::-2]) #output: (5, 3, 1) - The slicing a[::-2] creates a new tuple that includes every second element from the original tuple a but in reverse order. In this case, it starts from the last element (index -1) and includes every second element in reverse order, resulting in the output (5, 3, 1).  can be used to reverse a tuple and skip elements at the same time.


a = (1, 2, 3, 4, 5)
print(a[-1:-3]) #output: () - The slicing a[-1:-3] creates a new tuple that includes the elements from index -1 to index -2 (index -3 is excluded) of the original tuple a. However, since the starting index (-1) is greater than the ending index (-3), the slice does not include any elements and results in an empty tuple ().



