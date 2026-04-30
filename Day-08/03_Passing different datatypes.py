
#Passing the dufferent datatypes to the function-

#1.sending a list as an argument:

def my_function(names):
    for fruit in names:
        print(fruit)
my_function(["apple","banana","orange"]) #output: apple
                            #         banana
                            #         orange - In this example, we define a function my_function that takes a parameter names. When we call the function with a list of fruits (["apple", "banana", "orange"]), it iterates through the list and prints each fruit on a new line.

#2.sending a tuple as an argument:

def my_function(names):
    for fruit in names:
        print(fruit)
my_function(("apple","banana","orange")) #output: apple
                            #         banana
                            #         orange - In this example, we define a function my_function that takes a parameter names. When we call the function with a tuple of fruits (("apple", "banana", "orange")), it iterates through the tuple and prints each fruit on a new line. This demonstrates that we can pass different data types (like lists and tuples) as arguments to a function in Python.


#3.sending a dictionary as an argument:

def my_function(person):
    print("Name:", person["name"])
    print("Age:", person["age"])
my_function({"name": "Alice", "age": 30}) #output: Name: Alice
                                            #         Age: 30 - In this example, we define a function my_function that takes a parameter person. When we call the function with a dictionary ({"name": "Alice", "age": 30}), it accesses the values associated with the keys "name" and "age" in the dictionary and prints them. This demonstrates that we can pass a dictionary as an argument to a function in Python.



#4.sending a set as an argument:

def my_function(fruits):
    for fruit in fruits:
        print(fruit)
my_function({"apple", "banana", "orange"}) #output: apple
                            #         banana
                            #         orange - In this example, we define a function my_function that takes a parameter fruits. When we call the function with a set of fruits ({"apple", "banana", "orange"}), it iterates through the set and prints each fruit on a new line. This demonstrates that we can pass a set as an argument to a function in Python. Note that sets do not maintain order, so the output may vary in order each time you run the code.


#5.sending a string as an argument:

def my_function(name):
    print("Hello, " + name + "!")
my_function("Alice") #output: Hello, Alice! - In this example, we define a function my_function that takes a parameter name. When we call the function with a string argument ("Alice"), it concatenates the string "Hello, " with the value of name and an exclamation mark, resulting in printing "Hello, Alice!". This demonstrates that we can pass a string as an argument to a function in Python.


#6.returing different datatypes from a function:

def my_function():
    return [1, 2, 3], {"name": "Alice", "age": 30}, (4, 5, 6), "Hello"
result = my_function()
print(result) #output: ([1, 2, 3], {'name': 'Alice', 'age': 30}, (4, 5, 6), 'Hello') - In this example, we define a function my_function that returns multiple values of different data types: a list, a dictionary, a tuple, and a string. When we call the function and store the result in the variable result, it contains all the returned values as a tuple. When we print result, it shows the tuple containing the list, dictionary, tuple, and string. This demonstrates that a function can return multiple values of different data types in Python.


