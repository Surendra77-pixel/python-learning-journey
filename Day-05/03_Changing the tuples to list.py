
#changing the tuples to list -  

#1.we can convert a tuple to a list using the list() constructor. The list() constructor takes an iterable (like a tuple) as an argument and returns a new list containing the elements of that iterable. 

my_tuple = (1, "hello", 3.14, True)
my_list = list(my_tuple)
print(my_list) #output: [1, 'hello', 3.14, True] - The list() constructor converts the tuple my_tuple into a list and assigns it to the variable my_list. The resulting list contains the same elements as the original tuple, but it is now a mutable list that can be modified if needed.

fruits=("apple","banana","cherry")
fruit=list(fruits)
print(fruit) #output: ['apple', 'banana', 'cherry'] - The list() constructor converts the tuple fruits into a list and assigns it to the variable fruit. The resulting list contains the same elements as the original tuple, but it is now a mutable list that can be modified if needed.

