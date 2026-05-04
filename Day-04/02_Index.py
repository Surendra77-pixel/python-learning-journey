
#index list - we can access individual items in a list using their index. The index of the first item is 0, the second item is 1, and so on. We can also use negative indexing to access items from the end of the list, where the last item has an index of -1, the second to last item has an index of -2, and so on.

#1. using positive index - The first item has an index of 0, the second item has an index of 1, and so on.
fruits = ["apple", "banana", "cherry", "date", "fig"]
print(fruits[0]) #output: apple
print(fruits[1]) #output: banana
print(fruits[2]) #output: cherry
print(fruits[3]) #output: date
print(fruits[4]) #output: fig


#2.Negative indexing - The last item has an index of -1, the second to last item has an index of -2, and so on.
fruits = ["apple", "banana", "cherry", "date", "fig"]
print(fruits[-1]) #output: fig
print(fruits[-2]) #output: date
print(fruits[-3]) #output: cherry
print(fruits[-4]) #output: banana
print(fruits[-5]) #output: apple

#3.finding the index of an item  with index and position - we can use the index() method to find the index of the first occurrence of an item in a list. The index() method takes the item as an argument and returns its index. If the item is not found, it raises a ValueError. Here is an example:
fruits = ["apple", "banana", "cherry", "kiwi" ,"mango" ,"orange","cherry"]
print(fruits.index("cherry",4)) #output: 6 - The index() method is used to find the index of the first occurrence of the item "cherry" in the list fruits, starting the search from index 4. Since "cherry" is found at index 6, the method returns 6 as the output.
