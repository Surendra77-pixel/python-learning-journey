#Tuples -

# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets-().

#one of the main differences between lists and tuples is that tuples are immutable, meaning that once a tuple is created, its elements cannot be changed, added, or removed. This makes tuples more efficient than lists when it comes to memory usage and performance, especially when dealing with large datasets.

#no append, insert, remove, pop, clear ,extend, reverse, sort methods in tuples because they are immutable.

#The tuple is fater than the list because of its immutability. When a tuple is created, it is stored in a contiguous block of memory, which allows for faster access and retrieval of its elements. In contrast, a list is stored as a dynamic array, which can lead to slower performance when adding or removing elements.

#The tuple is used for fixed data that should not be changed, such as the days of the week, the months of the year, or the coordinates of a point in space. It is also used for data that needs to be hashed, such as keys in a dictionary or elements in a set.

#1. creating a tuple - You can create a tuple by placing a sequence of values separated by commas inside parentheses ().
my_tuple = (1, "hello", 3.14, True)
print(my_tuple) #output: (1, 'hello', 3.14, True)

#2.we can create a tuple without using parentheses, just by separating the values with commas.
my_tuple = 1, "hello", 3.14, True
print(my_tuple) #output: (1, 'hello', 3.14, True)

#3.single element tuple - To create a tuple with a single element, you need to include a comma after the element, otherwise it will be treated as a regular value.
my_tuple = (1,)
print(my_tuple) #output: (1,)

#There are only the 2 methods in the tuple - count() and index() methods.   

#tuples use less memory than lists because of their immutability. When a tuple is created, it is stored in a contiguous block of memory, which allows for faster access and retrieval of its elements. In contrast, a list is stored as a dynamic array, which can lead to slower performance when adding or removing elements. Additionally, since tuples are immutable, they can be optimized by the Python interpreter, resulting in even faster performance compared to lists.

#used in the databases , fixed data , function 

#rules in tuples -------------------------------------

#1.immutable- once a tuple is created, its elements cannot be changed, added, or removed. This means that you cannot modify the contents of a tuple after it has been created. If you need to change the contents of a tuple, you will need to create a new tuple with the desired changes.

#2.ordered - the order of the items in a tuple is preserved and they can be accessed using their index.

#3. allows duplicate values - a tuple can contain duplicate values, meaning that the same value can appear multiple times in a tuple.

#4.support indexing and slicing - you can access individual elements of a tuple using their index, and you can also slice a tuple to create a new tuple that contains a subset of the original elements.
#5.can store different data types - a tuple can contain elements of different data types, such as integers, strings, and booleans.

#6.faster than list because of immutability - When a tuple is created, it is stored in a contiguous block of memory, which allows for faster access and retrieval of its elements. In contrast, a list is stored as a dynamic array, which can lead to slower performance when adding or removing elements. Additionally, since tuples are immutable, they can be optimized by the Python interpreter, resulting in even faster performance compared to lists.

#7.single element tuple can be done with comma 


#.Small logic with tuples-------------------

#1.tuple length - 

# we can use the len() function to get the length of the tuple:
my_tuple = (1, "hello", 3.14, True)
print(len(my_tuple)) #output: 4

#2.type() function to check the type of the tuple:
my_tuple = (1, "hello", 3.14, True)
print(type(my_tuple)) #output: <class 'tuple'>


#3.tuple datatypes - 

#  we can create a tuple with different data types, such as integers, strings, and booleans: 
my_tuple=("Apple","banana","cherry")
my_tuple2=(1,2,3,4)
my_tuple3=(True,False,True)
print(my_tuple) #output: ('Apple', 'banana', 'cherry')
print(my_tuple2) #output: (1, 2, 3, 4)
print(my_tuple3) #output: (True, False, True)

#4.tuple constructor -

#  we can use the tuple() constructor to create a tuple from an iterable (like a string, list, or another tuple):
my_string = "hello"
my_tuple = tuple(my_string)
print(my_tuple) #output: ('h', 'e', 'l', 'l', 'o')

tuple =tuple(("Surendra","manthri","20","hyderabad"))
print(tuple) #output: ('Surendra', 'manthri', '20', 'hyderabad')

#what is the constructor in python -

#  a constructor is a special method that is called when an object is created. It is used to initialize the attributes of the object and set up any necessary resources. In Python, the constructor method is defined using the __init__() method, which takes self as its first parameter and can also take additional parameters to initialize the object's attributes. we cna change list to tuple and tuple to list using the constructor.

fruits = ["apple", "banana", "cherry", "orange", "grape"]
print(fruits[::2])
#output: ['apple', 'cherry', 'grape'] - The slicing syntax [::2] is used to create a new list that includes every second element from the original list. In this case, it starts from the first element (index 0) and includes every second element, resulting in the output ['apple', 'cherry', 'grape'].

num=(1,2,3,4,5)
print(num[::2])
#output: (1, 3, 5) - The slicing syntax [::2] is used to create a new tuple that includes every second element from the original tuple. In this case, it starts from the first element (index 0) and includes every second element, resulting in the output (1, 3, 5).


