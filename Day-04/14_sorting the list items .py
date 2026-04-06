
#1,sorting the list items - The sort() method is used to sort the items of a list in ascending order. It modifies the original list in place.

fruits = ["banana", "apple", "cherry"]
fruits.sort()
print(fruits) #output: ['apple', 'banana', 'cherry']

age = [40, 25, 35, 30]
age.sort()
print(age) #output: [25, 30, 35, 40]

#1.2.other way to sort a list is using the sorted() function - The sorted() function is a built-in function that returns a new sorted list from the items in an iterable. It does not modify the original list.
fruits = ["banana", "apple", "cherry"]  
sorted_fruits = sorted(fruits)
print(sorted_fruits) #output: ['apple', 'banana', 'cherry']

#2.descending order- You can sort a list in descending order by passing the reverse=True argument to the sort() method or the sorted() function. to sort the descending use the keyword arugument reverse=True
fruits = ["banana", "apple", "cherry"]
sorted_fruits_desc = sorted(fruits, reverse=True)
print(sorted_fruits_desc) #output: ['cherry', 'banana', 'apple']

age = [40, 25, 35, 30]
sorted_age = sorted(age, reverse=True)
print(sorted_age) #output: [40, 35, 30, 25]

#2.1other way to sort in descending order - You can also sort a list in descending order by passing the reverse=True argument to the sort() method or the sorted() function. to sort the descending use the keyword arugument reverse=True

fruits = ["banana", "apple", "cherry"]
sorted_fruits_desc = sorted(fruits, reverse=True)
print(sorted_fruits_desc) #output: ['cherry', 'banana', 'apple']

age = [40, 25, 35, 30]
sorted_age_desc = sorted(age, reverse=True)
print(sorted_age_desc) #output: [40, 35, 30, 25]


#3.case insensitive sorting - By default, the sort() method and the sorted() function sort strings in a case-sensitive manner, which means that uppercase letters are sorted before lowercase letters. If you want to sort strings in a case-insensitive manner, you can use the key parameter and pass the str.lower function as the key.
fruits = ["banana", "Apple", "cherry"]
sorted_fruits_case_insensitive = sorted(fruits, key=str.lower)
print(sorted_fruits_case_insensitive) #output: ['Apple', 'banana', 'cherry']
