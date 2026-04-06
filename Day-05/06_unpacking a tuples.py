#Unpacking a tuple ----------

#when we create a tuple normally assign values to it this called packing a tuple 
my_tuple = (1, "hello", 3.14, True) 
print(my_tuple) #output: (1, 'hello', 3.14, True) - The variable my_tuple is assigned a tuple containing the values 1, "hello", 3.14, and True. This process of creating a tuple and assigning it to a variable is known as packing a tuple.

#1.unpacking a tuple - we can also unpack the elements of a tuple into separate variables. This is done by assigning the tuple to a comma-separated list of variables. Here is an example:
my_tuple = (1, "hello", 3.14, True)
a, b, c, d = my_tuple
print(a) #output: 1 - The variable a is assigned the value of the first
print(b) #output: 'hello' - The variable b is assigned the value of the second element of the tuple my_tuple, which is 'hello'.
print(c) #output: 3.14 - The variable c is assigned the value of the third element of the tuple my_tuple, which is 3.14.
print(d) #output: True - The variable d is assigned the value of the fourth element of the tuple my_tuple, which is True.

