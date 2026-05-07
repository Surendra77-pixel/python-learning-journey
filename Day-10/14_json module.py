
#                       json module and its functions in Python

#The json module in Python provides functions for working with JSON (JavaScript Object Notation) data. JSON is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate. The json module allows you to convert Python objects to JSON format and vice versa.

#Some common functions provided by the json module include:

#1.dumps():
#The json.dumps() function is used to convert a Python object into a JSON string. It takes a Python object as input and returns a JSON-formatted string. For example, you can use json.dumps() to convert a Python dictionary into a JSON string:
import json
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
json_string = json.dumps(my_dict)   
print(json_string) #Output- {"name": "Alice", "age": 30, "city": "New York"}
#explanation- In the above code, we have imported the json module and created a Python dictionary called my_dict. We then use the json.dumps() function to convert the dictionary into a JSON-formatted string, which is stored in the variable json_string. When we print json_string, it returns a string representation of the JSON data, which includes the keys and values from the original dictionary in JSON format.


#2.loads():
#The json.loads() function is used to parse a JSON string and convert it into a Python object. It takes a JSON-formatted string as input and returns the corresponding Python object. For example, you can use json.loads() to convert a JSON string back into a Python dictionary:
import json
json_string = '{"name": "Alice", "age": 30, "city": "New York"}'
my_dict = json.loads(json_string)
print(my_dict) #Output- {'name': 'Alice', 'age': 30, 'city': 'New York'}
#explanation- In the above code, we have imported the json module and defined a JSON-formatted string called json_string. We then use the json.loads() function to parse the JSON string and convert it back into a Python dictionary, which is stored in the variable my_dict. When we print my_dict, it returns a Python dictionary that contains the same keys and values as the original JSON string.

#3.dump():
#The json.dump() function is used to write a Python object to a file in JSON format. It takes a Python object and a file object as input and writes the JSON representation of the object to the file. For example, you can use json.dump() to write a Python dictionary to a JSON file:
import json
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
with open('data.json', 'w') as file:
    json.dump(my_dict, file) #This will write the JSON representation of my_dict to data.json 
#In the above code, we have imported the json module and created a Python dictionary called my_dict. We then use a with statement to open a file called data.json in write mode ('w') and pass the file object to the json.dump() function along with the dictionary. The json.dump() function writes the JSON representation of my_dict to the file, which can be read later using json.load() or by opening the file directly.


#4.load():
#The json.load() function is used to read a JSON-formatted file and convert it into a Python object. It takes a file object as input and returns the corresponding Python object. For example, you can use json.load() to read a JSON file and convert it back into a Python dictionary:
import json
with open('data.json', 'r') as file:
    my_dict = json.load(file) #This will read the JSON data from data.json and convert it into a Python dictionary
print(my_dict) #Output- {'name': 'Alice', 'age': 30, 'city': 'New York'}
#In the above code, we have imported the json module and used a with statement to open the file data.json in read mode ('r'). We then pass the file object to the json.load() function, which reads the JSON data from the file and converts it into a Python dictionary. The resulting dictionary is stored in the variable my_dict, which is then printed to the console, showing the same keys and values as the original JSON data that was written to the file.


#5.JSONEncoder and JSONDecoder:
#The json module also provides the JSONEncoder and JSONDecoder classes, which can be used to customize the encoding and decoding of JSON data. The JSONEncoder class allows you to define how Python objects are converted to JSON format, while the JSONDecoder class allows you to define how JSON data is converted back into Python objects. For example, you can create a custom JSONEncoder to handle a specific type of Python object:
import json
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)  # Convert sets to lists for JSON serialization
        return super().default(obj)
my_set = {1, 2, 3}
json_string = json.dumps(my_set, cls=CustomEncoder)  # Use the custom encoder
print(json_string) #Output- [1, 2, 3]
#In the above code, we have defined a CustomEncoder class that inherits from json.JSONEncoder. We override the default() method to check if the object being encoded is a set, and if so, we convert it to a list before encoding it as JSON. This allows us to serialize sets in JSON format, which is not natively supported by the json module.

