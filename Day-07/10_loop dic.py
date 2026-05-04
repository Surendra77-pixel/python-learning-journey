#loops through a dictionary

#1.for loop-

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
for key in my_dict:
    print(key) #output: name, age, city - The for loop iterates through each key in the dictionary my_dict and prints it. Each key is printed on a new line.
for key, value in my_dict.items():
    print(f"{key}: {value}") #output: name: Alice, age: 30, city: New York - The for loop iterates through each key-value pair in the dictionary my_dict using the items() method. It prints each key and its corresponding value in the format "key: value". Each key-value pair is printed on a new line.

#2.while loop-

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
keys = list(my_dict.keys())
i = 0
while i < len(keys):
    key = keys[i]
    value = my_dict[key]
    print(f"{key}: {value}") #output: name: Alice, age: 30, city: New York - The while loop iterates through the list of keys in the dictionary my_dict. It uses an index variable i to access each key and its corresponding value. The loop continues until it has processed all keys in the dictionary, printing each key-value pair in the format "key: value" on a new line.
    i += 1


