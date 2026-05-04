#Data types define the type of value a variable can store.They tell Python what kind of data you are working with.

#Python has several built-in data types, including:

                    #Numeric types: int (integer)

x=5
print(x) # Output: 5

                 #string types: str (string)

y="Hello, World!"
print(y) # Output: Hello, World!

                #float types: float (floating-point number)

z=3.14
print(z) # Output: 3.14

                 #complex types: complex (complex number)

x=2+3j
print(x) # Output: (2+3j)

                #boolean types: bool (boolean)

is_true=True
print(is_true) # Output: True

                #list types: list (ordered collection of values)

my_list=[1,2,3,4,5]
print(my_list) # Output: [1, 2, 3, 4,   

                #tuple types: tuple (ordered collection of values that cannot be changed)

my_tuple=(1,2,3,4,5)
print(my_tuple) # Output: (1, 2, 3, 4, 5)

                #range types: range (represents a sequence of numbers)

my_range=range(1,10)
print(my_range) # Output: range(1, 10)

               #dictionary types: dict (collection of key-value pairs)

my_dict={"name":"Alice","age":30,"city":"New York"}
print(my_dict) # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

               #set types: set (collection of unique values)

my_set={1,2,3,4,5}
print(my_set) # Output: {1, 2, 3, 4, 5}

            #frozenset types: frozenset (immutable set)

my_frozenset=frozenset([1,2,3,4,5])
print(my_frozenset) # Output: frozenset({1, 2, 3, 4, 5})

            #bytes types: bytes (immutable sequence of bytes)

my_bytes=b'Hello, World!'
print(my_bytes) # Output: b'Hello, World!'

             #MEMORY views: memoryview (memory view object)

my_memoryview=memoryview(b'Hello, World!')
print(my_memoryview) # Output: <memory at 0x7f8c8c8c8c8c>

            #none types: NoneType (represents the absence of a value)
            
my_none=None
print(my_none) # Output: None


#how to check the particular data type of a variable in python we can use the built-in type() function to check the data type of a variable. Here are some examples:

x="Surendra"
print(type(x)) # Output: <class 'str'> # This datatype defines a string so it shows the string data type

                           #random number-

#python do not have random() function but it has a random module that contains a random() function which can be used to generate random numbers. Here is an example:
import random
print(random.Random.randrange(1,10)) # type: ignore # Output: A random number between 1 and 10 (inclusive).