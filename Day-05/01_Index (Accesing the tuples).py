
#accesing the tuples -



#1.indexing - 

# we can access individual elements of a tuple using their index. The index starts from 0 for the first element, 1 for the second element, and so on. We can also use negative indexing to access elements from the end of the tuple, where -1 refers to the last element, -2 refers to the second last element, and so on. Here is an example:

my_tuple = (1, "hello", 3.14, True)
print(my_tuple[0]) #output: 1 - The indexing my_tuple[0]
print(my_tuple[1]) #output: 'hello' - The indexing my_tuple[1]
print(my_tuple[2]) #output: 3.14 - The indexing my_tuple[2]
print(my_tuple[3]) #output: True - The indexing my_tuple[3]
print(my_tuple[-1]) #output: True - The negative indexing my_tuple[-1]
print(my_tuple[-2]) #output: 3.14 - The negative indexing my_tuple[-2]
print(my_tuple[-3]) #output: 'hello' - The negative indexing my_tuple[-3]
print(my_tuple[-4]) #output: 1 - The negative indexing my_tuple[-4]


#2.searching with the index and with position -

fruits = ("apple", "banana", "cherry", "date", "elderberry" ,"cherry")
print(fruits.index("cherry",  4)) #output: 5 - The index() method is used to find the index of the first occurrence of the item "cherry" in the tuple fruits, starting the search from index 4. Since "cherry" is found at index 5, the method returns 5 as the output.