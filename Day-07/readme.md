📅 Day 07 – Python Dictionaries Mastery
📌 What I Learned Today

Today I focused on Python Dictionaries, one of the most powerful data structures used to store data in key-value pairs

🧠 Core Concepts
🔹 What is a Dictionary?
A dictionary stores data in key : value format
Keys are unique & immutable (string, int, tuple)
Values can be any data type
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
🔹 Accessing Dictionary Items
Using keys
Using .get() (safe method)
print(my_dict["name"])
print(my_dict.get("country", "Not Found"))

👉 Learned that direct access gives error, but get() avoids it

🔹 Adding Items
my_dict["city"] = "New York"

👉 Adds new key-value pair dynamically

🔹 Updating Items
my_dict["age"] = 31
my_dict.update({"city": "Los Angeles"})

👉 Learned both direct update & .update() method

🔹 Removing Items
pop() → removes specific key
popitem() → removes last/random item
del → delete key or whole dictionary
clear() → empty dictionary
my_dict.pop("age")
del my_dict["city"]
my_dict.clear()

👉 Different removal techniques and when to use them

🔹 Checking if Key Exists
if "age" in my_dict:
    print("Exists")

👉 Used in keyword for validation

🔹 Dictionary Methods
.keys()
.values()
.items()
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

👉 Learned that these return dynamic views

🔹 Convert Dictionary to List
list(my_dict.keys())
list(my_dict.values())
list(my_dict.items())

👉 Converted dictionary data into list format

🔹 Copying Dictionary
new_dict = my_dict.copy()
new_dict2 = dict(my_dict)

👉 Learned about shallow copy concept

🔹 Looping Through Dictionary
for key, value in my_dict.items():
    print(key, value)

👉 Also practiced while loop iteration

🔹 Nested Dictionary
student = {
    "name": "John",
    "address": {
        "city": "NY"
    }
}

👉 Accessed using multiple keys

🔹 Dictionary Comprehension
squares = {num: num**2 for num in range(5)}

👉 Created dictionary using one-line logic

🚀 Mini Project – Smart Dictionary

I built a CLI-based Dictionary App with:

Features:
➕ Add Word
🔍 Search Word
🔄 Update Word
🗑️ Delete Word
📖 Display All Words

👉 Used:

Loops (while)
Conditions (if-else)
Dictionary operations

📌 Example snippet:

dictionary[word] = meaning


💡 Key Takeaways
Dictionaries are fast & efficient for lookup
Keys must be unique
.get() is safer than direct access
.items() is best for looping
Learned real-world usage through project
🧩 Example Sentence-

👉 “Dictionary is like a phonebook — you search by name (key) and get the number (value).”