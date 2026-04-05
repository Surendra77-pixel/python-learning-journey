
#finding index of an item in a list


#1. using the index() method - The index() method is used to find the index of the first occurrence of a specific item in a list. It takes an item as an argument and returns the index of the first occurrence of that item in the list. If the item is not found, it raises a ValueError.
fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana")) #output: 1



age = [25, 30, 35, 40]
print(age.index(35)) #output: 2


fruits = ["apple", "banana", "cherry"]
print(fruits.index("grape")) #output: ValueError: 'grape' is not in list

#2. using a loop - You can also use a loop to iterate through the list and find the index of a specific item. This method is useful if you want to find the index of all occurrences of an item in the list.
fruits = ["apple", "banana", "cherry", "banana"]
item_to_find = "banana"
indices = []
for index in range(len(fruits)):
    if fruits[index] == item_to_find:
        indices.append(index)
print(indices) #output: [1, 3]

