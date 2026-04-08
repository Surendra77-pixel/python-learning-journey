
#checking an item in a dictionary - we can check if a key is present in a dictionary using the in keyword. Here is an example:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
if "age" in my_dict:
    print("Key 'age' is present in the dictionary.")
else:
    print("Key 'age' is not present in the dictionary.")   


if "country" in my_dict:
    print("Key 'country' is present in the dictionary.")
else:    print("Key 'country' is not present in the dictionary.")
#output: Key 'age' is present in the dictionary. - The if statement checks if the key "age" is present in the dictionary my_dict using the in keyword, and since it is found, it executes the print statement indicating that the key is present in the dictionary.
#output: Key 'country' is not present in the dictionary. - The if statement checks if the key "country" is present in the dictionary my_dict using the in keyword, and since it is not found, it executes the else block and prints a message indicating that the key is not present in the dictionary. 


