
#slicing - slicing is a powerful feature in Python that allows you to access a portion of a list or a range of items in a list. It is done using the slicing syntax, which is list[start:end] or list[start:end:step].

#example of slicing a list using a list of indexes -

fruits = ("apple", "banana", "cherry", "date", "fig",
            "grape", "kiwi", "lemon", "mango", "orange")

print(fruits[-4:-1]) #output: ['lemon', 'mango', 'orange']

print(fruits[-5:-2]) #output: ['kiwi', 'lemon', 'mango']

print(fruits[-3:]) #output: ['mango', 'orange']

print(fruits[:-3]) #output: ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi']   

print(fruits[:]) #output: ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi', 'lemon', 'mango', 'orange']

print(fruits[-1::-1]) #output: ['orange', 'mango', 'lemon', 'kiwi', 'grape', 'fig', 'date', 'cherry', 'banana', 'apple'] this and the reverse method like the -

print(fruits[::-1]) #are the same methods 

print(fruits[1::2]) #output: ['banana', 'date', 'grape', 'lemon', 'orange'] - The slicing fruits[1::2] creates a new list that includes every second element from the original list fruits, starting from index 1. In this case, it includes the elements at index 1 and index 3, resulting in the output ['banana', 'date', 'grape', 'lemon', 'orange'].

print(fruits[::2]) #output: ['apple', 'cherry', 'fig', 'kiwi', 'mango'] - The slicing fruits[::2] creates a new list that includes every second element from the original list fruits. In this case, it starts from the first element (index 0) and includes every second element, resulting in the output ['apple', 'cherry', 'fig', 'kiwi', 'mango'].

print(fruits[::-2]) #output: ['orange', 'lemon', 'grape', 'date', 'apple'] - The slicing fruits[::-2] creates a new list that includes every second element from the original list fruits, but in reverse order. It starts from the last element (index -1) and moves backwards, including every second element, resulting in the output ['orange', 'lemon', 'grape', 'date', 'apple'].

