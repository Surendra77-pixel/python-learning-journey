
#                         json module

# The json is known as the javascript object notation it is a format used to store and transfer data 

#python uses the built-in json module to work with json data. -
import json

#it is a data format used to store and exchange data between a server and a client. It is a lightweight data-interchange format that is easy for humans to read and write, and easy for machines to parse and generate.example-

#1.python programs
#2.apis
#3.web applications
#4.configuration files
#5.data storage -- Think of like a digital notebook where you can store and organize your data in a structured way. It allows you to easily access and manipulate the data when needed.

#example-

{
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

#The above one is the json data in this the python can readit , write it and save it into files , send it to websites and apis and also receive it from websites and apis and also use it for data storage. The json module in python provides functions to work with json data, such as json.dumps() for converting python objects to json strings, and json.loads() for converting json strings back to python objects. You can also use json.dump() and json.load() for working with files that contain json data.


#In json there are two main data structures:

#1.objects - An object is a collection of key-value pairs, where each key is a string and the value can be any valid json data type (e.g., string, number, array, object, boolean, null). Objects are enclosed in curly braces {}. Example:
{
    "name": "Alice",
    "age": 25,
    "city": "Los Angeles"
}

#2.arrays - An array is an ordered list of values, where each value can be any valid json data type. Arrays are enclosed in square brackets []. Example:
[
    "apple",
    "banana",
    "orange"
]


#in the json there are some data types that are used to represent different types of data:

#1.string - A sequence of characters enclosed in double quotes. Example: "Hello, World!"
#2.number - A numeric value that can be an integer or a floating-point number. Example: 42, 3.14
#3.object - A collection of key-value pairs enclosed in curly braces {}. Example: {"name": "Alice", "age": 25}
#4.array - An ordered list of values enclosed in square brackets []. Example: ["apple", "banana", "orange"]
#5.boolean - A value that can be either true or false. Example: true, false
#6.null - A value that represents the absence of a value. Example: null
#7.array - An ordered list of values enclosed in square brackets []. Example: ["apple", "banana", "orange"]
#8.object - A collection of key-value pairs enclosed in curly braces {}. Example: {"name": "Alice", "age": 25}

#1.json string -

#  A json string is a string that contains json data. It can be created by using the json.dumps() function to convert a python object into a json string. Example:
import json
data = {
    "name": "Alice",
    "age": 25,
    "city": "Los Angeles"
}


#2.json number -

# A json number is a numeric value that can be an integer or a floating-point number. It is represented in json as a sequence of digits, optionally preceded by a minus sign and followed by an optional decimal point and more digits. Example: 42, 3.14
import json
number = 42
json_number = json.dumps(number)  # Convert the number to a json string
print(json_number)  # Output: 42


#3.json boolean -

# A json boolean is a value that can be either true or false. It is represented in json as the literals true and false. Example: true, false
import json
boolean_value = True
json_boolean = json.dumps(boolean_value)  # Convert the boolean value to a json string
print(json_boolean)  # Output: true


#3.json null -

# A json null is a value that represents the absence of a value. It is represented in json as the literal null. Example: null
import json
null_value = None
json_null = json.dumps(null_value)  # Convert the null value to a json string
print(json_null)  # Output: null


#4.json array -

# A json array is an ordered list of values enclosed in square brackets []. Each value can be any valid json data type. Example: ["apple", "banana", "orange"]
import json
array = ["apple", "banana", "orange"]
json_array = json.dumps(array)  # Convert the array to a json string
print(json_array)  # Output: ["apple", "banana", "orange"]


#5.json object -

# A json object is a collection of key-value pairs enclosed in curly braces {}. Each key is a string and the value can be any valid json data type. Example: {"name": "Alice", "age": 25}
import json
obj = {
    "name": "Alice",
    "age": 25,
    "city": "Los Angeles"
}
json_object = json.dumps(obj)  # Convert the object to a json string
print(json_object)  # Output: {"name": "Alice", "age": 25, "city": "Los Angeles"}


#                            dumps() and the dump()

#What are the dumps and the dump functions in the json module??

# The dumps() function converts a Python object into a JSON string.
# The dump() function writes a Python object as JSON to a file-like object.

#Example of using json.dumps() to convert a Python object to a JSON string:

import json
data = {
    "name": "Alice",
    "age": 25,
    "city": "Los Angeles"
}
json_string = json.dumps(data)
print(json_string)  # Output: {"name": "Alice", "age": 25, "city": "Los Angeles"}
#explanation: In this example, we have a Python dictionary called data. We use the json.dumps() function to convert this dictionary into a JSON string, which is then printed to the console.

#Example of using json.dump() to write a Python object as JSON to a file:

import json
data = {
    "name": "Alice",
    "age": 25,
    "city": "Los Angeles"
}
with open('data.json', 'w') as file:
    json.dump(data, file)
#output: A file named data.json will be created (or overwritten if it already exists) with the following content:
#{"name": "Alice", "age": 25, "city": "Los Angeles"}
#explanation: In this example, we have the same Python dictionary called data. We use the json.dump() function to write this dictionary as JSON to a file named data.json. The file will contain the JSON representation of the data dictionary.


#The json loads() and the load() functions are used to parse JSON data and convert it back into Python objects.

#1.json loads() -

# The json.loads() function takes a JSON string as input and returns the corresponding Python object. It is used to parse a JSON string and convert it into a Python data structure (e.g., dictionary, list, etc.). Example:

import json
json_string = '{"name": "Alice", "age": 25, "city": "Los Angeles"}'
data = json.loads(json_string)
print(data)  # Output: {'name': 'Alice', 'age': 25, 'city': 'Los Angeles'}
#explanation: In this example, we have a JSON string that represents a dictionary. We use the json.loads() function to parse this JSON string and convert it into a Python dictionary, which is then printed to the console.

#2.json load() -

# The json.load() function takes a file-like object containing JSON data and returns the corresponding Python object. It is used to read JSON data from a file and convert it into a Python data structure. Example:

import json
with open('data.json', 'r') as file:
    data = json.load(file)
print(data)  # Output: {'name': 'Alice', 'age': 25, 'city': 'Los Angeles'}
#explanation: In this example, we open a file named data.json that contains JSON data. We use the json.load() function to read the JSON data from the file and convert it into a Python dictionary, which is then printed to the console. The file should contain valid JSON data for this to work correctly.   

# in short we can say-

#1.json.dumps() - Converts a Python object into a JSON string.

#2.json.dump() - Writes a Python object as JSON to a file-like object.

#3.json.loads() - Parses a JSON string and converts it into a Python object.

#4.json.load() - Reads JSON data from a file-like object and converts it into a Python object.


