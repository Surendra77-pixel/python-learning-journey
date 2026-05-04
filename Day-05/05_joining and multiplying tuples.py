
#Joining the tuples ----------

#1.joining two tuples -
# we can join two tuples together using the + operator. This creates a new tuple that contains all the elements of both tuples. Here is an example:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
joined_tuple = tuple1 + tuple2
print(joined_tuple) #output: (1, 2, 3, 4, 5, 6) - The + operator is used to join the two tuples tuple1 and tuple2 together, resulting in a new tuple joined_tuple that contains all the elements of both tuples.

#2.joining multiple tuples - we can also join more than two tuples together using the + operator. Here is an example:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = (7, 8, 9)
joined_tuple = tuple1 + tuple2 + tuple3
print(joined_tuple) #output: (1, 2, 3, 4, 5, 6, 7, 8, 9) - The + operator is used to join the three tuples tuple1, tuple2, and tuple3 together, resulting in a new tuple joined_tuple that contains all the elements of the three tuples.   


#3.multiplying tuples - we can also multiply a tuple by an integer using the * operator. This creates a new tuple that contains the elements of the original tuple repeated a specified number of times. Here is an example:
my_tuple = (1, 2, 3)
multiplied_tuple = my_tuple * 3
print(multiplied_tuple) #output: (1, 2, 3, 1, 2, 3, 1, 2, 3) - The * operator is used to multiply the tuple my_tuple by the integer 3, resulting in a new tuple multiplied_tuple that contains the elements of my_tuple repeated three times.

#4.multiplying with negative integer - if we multiply a tuple by a negative integer, it will result in an empty tuple. Here is an example:
my_tuple = (1, 2, 3)
multiplied_tuple = my_tuple * -2
print(multiplied_tuple) #output: () - The * operator is used to multiply the tuple my_tuple by the negative integer -2, resulting in an empty tuple multiplied_tuple. This is because multiplying a tuple by a negative integer does not make sense in terms of repetition, and therefore it results in an empty tuple.

