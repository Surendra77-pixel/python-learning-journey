
#slicing - Slicing is a powerful feature in Python that allows you to access a portion of a list or a range of items in a list. It is done using the slicing syntax, which is list[start:end] or list[start:end:step].
 
#1. slicing items from a list or range of indexes - You can access a range of items in a list by using the slicing syntax. The syntax for slicing is list[start:end], where start is the index of the first item you want to access and end is the index of the item you want to stop at (but not include).
fruits = ["apple", "banana", "cherry", "date", "fig"]
print(fruits[1:4]) #output: ['banana', 'cherry', 'date']
print(fruits[0:3]) #output: ['apple', 'banana', 'cherry']
print(fruits[2:]) #output: ['cherry', 'date', 'fig
print(fruits[:3]) #output: ['apple', 'banana', 'cherry']
print(fruits[:]) #output: ['apple', 'banana', 'cherry', 'date', 'fig']


#2.slicing items from a list or range of indexes with step - You can also specify a step in slicing to access every nth item in the list. The syntax for slicing with a step is list[start:end:step].
fruits = ["apple", "banana", "cherry", "date", "fig",
            "grape", "kiwi", "lemon", "mango", "orange"]
print(fruits[::2]) #output: ['apple', 'cherry', 'fig', 'kiwi', 'mango']
print(fruits[1::2]) #output: ['banana', 'date', 'grape', 'lemon', 'orange']
print(fruits[1:8:3]) #output: ['banana', 'date', 'lemon']#explanation: In this code, we have a list of fruits. We use slicing with a step to access every second item in the list. The first print statement accesses every second item starting from the first item (index 0), resulting in ['apple', 'cherry', 'fig', 'kiwi', 'mango']. The second print statement accesses every second item starting from the second item (index 1), resulting in ['banana', 'date', 'grape', 'lemon', 'orange']. The third print statement accesses every third item starting from the second item (index 1) up to index 8, resulting in ['banana', 'date', 'lemon'].


#3.slicing items from  from a list using the negative index - uou can also use negative indices in sliing to access a range of items in a list. The syntax for slicing with thw nwgative indices is list[start:end:step], where start and end can be negative indices.
fruits = ["apple", "banana", "cherry", "date", "fig",
            "grape", "kiwi", "lemon", "mango", "orange"]
print(fruits[-4:-1]) #output: ['lemon', 'mango', 'orange']
print(fruits[-5:-2]) #output: ['kiwi', 'lemon', 'mango']
print(fruits[-3:]) #output: ['mango', 'orange']
print(fruits[:-3]) #output: ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi']   
print(fruits[:]) #output: ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi', 'lemon', 'mango', 'orange']
print(fruits[-1::-1]) #output: ['orange', 'mango', 'lemon', 'kiwi', 'grape', 'fig', 'date', 'cherry', 'banana', 'apple']

