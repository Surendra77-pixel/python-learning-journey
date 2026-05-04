
# 1.The modifying lists - Lists in Python are mutable, which means you can change their content after they have been created. You can add, remove, or modify elements in a list using various methods and operations.

#1.to change the value of a specific item in a list, you can use indexing to access the item and assign it a new value. The syntax for changing an item in a list is list[index] = new_value, where index is the position of the item you want to change and new_value is the new value you want to assign to that item.

fruits = ["apple", "banana", "cherry", "date", "fig"]
fruits[1] = "blueberry"
print(fruits) #output: ['apple', 'blueberry', 'cherry', 'date', 'fig']C

Thelist=["Apple","banana","cherry","date","fig"]
Thelist[2]="grape"
print(Thelist) #output: ['Apple', 'banana', 'grape', 'date', 'fig']



#3.changing multiple items in a list - You can also change multiple items in a list at once by using slicing to access a range of items and assigning them new values. The syntax for changing multiple items in a list is list[start:end] = new_values, where start is the index of the first item you want to change, end is the index of the item you want to stop at (but not include), and new_values is a list of new values you want to assign to that range of items.
fruits = ["apple", "banana", "cherry", "date", "fig"]
fruits[1:4] = ["blueberry", "grape", "kiwi"]
print(fruits) #output: ['apple', 'blueberry', 'grape', 'kiwi', 'fig']

#4.when the length of the list will chnage when the number of items inserted does not match the number of items being replaced. If you insert more items than you replace, the list will grow in size. If you insert fewer items than you replace, the list will shrink in size.
fruits = ["apple", "banana", "cherry", "date", "fig"]
fruits[1:4] = ["blueberry", "grape"]
print(fruits) #output: ['apple', 'blueberry', 'grape', 'fig']


#5.when you insert more items than you replace, the list will grow in size. If you insert fewer items than you replace, the list will shrink in size.
fruits = ["apple", "banana", "cherry", "date", "fig"]
fruits[1:4] = ["blueberry"]
print(fruits) #output: ['apple', 'blueberry', 'fig']




