
#                             Array

#1. What is an array?

#An array is a data structure that can hold a fixed number of values of the same type. It is a collection of elements that are stored in contiguous memory locations. Arrays are used to store multiple values in a single variable, instead of declaring separate variables for each value. In Python, we can use the built-in list data type to create arrays.

#Python does not have a built-in array data type, but we can use the list data type to create arrays. Lists are mutable, which means that we can change their contents after they have been created. We can create a list by enclosing a comma-separated sequence of values in square brackets []. For example, we can create a list of integers like this:

my_array = [1, 2, 3, 4, 5]
print(my_array)
#Output-
#[1, 2, 3, 4, 5]

#2. We can also create a list of strings like this:

my_array = ["apple", "banana", "cherry"]
print(my_array)
#Output-
#['apple', 'banana', 'cherry']

#3.Acces elements of an array-
my_array = [1, 2, 3, 4, 5]
print(my_array[0]) #Output- 1
print(my_array[1]) #Output- 2
print(my_array[2]) #Output- 3
print(my_array[3]) #Output- 4
print(my_array[4]) #Output- 5

#4. We can also use negative indexing to access elements from the end of the list. For example, my_array[-1] will give us the last element of the list, which is 5 in this case.
print(my_array[-1]) #Output- 5
print(my_array[-2]) #Output- 4
print(my_array[-3]) #Output- 3
print(my_array[-4]) #Output- 2
print(my_array[-5]) #Output- 1

#5.The len() function can be used to get the number of elements in a list. For example, len(my_array) will return 5, which is the number of elements in the list.

print(len(my_array)) #Output- 5

#6. We can also use the append() method to add elements to the end of the list. For example, my_array.append(6) will add the number 6 to the end of the list.

my_array.append(6)
print(my_array) #Output- [1, 2, 3, 4, 5, 6]

#7. We can also use the insert() method to add elements at a specific index in the list. For example, my_array.insert(0, 0) will add the number 0 at index 0 of the list.

my_array.insert(0, 0)
print(my_array) #Output- [0, 1, 2, 3, 4, 5, 6]


#8. We can also use the remove() method to remove an element from the list. For example, my_array.remove(3) will remove the number 3 from the list.the list remove only removes the first occurrence of the specified value. If the value is not found in the list, it raises a ValueError. In this case, since 3 is present in the list, it will be removed successfully.

my_array.remove(3)
print(my_array) #Output- [0, 1, 2, 4, 5, 6]

#9. We can also use the pop() method to remove an element from the list and return it. For example, my_array.pop(0) will remove the first element of the list and return it.
first_element = my_array.pop(0)
print(first_element) #Output- 0
print(my_array) #Output- [1, 2, 4, 5, 6]

#10. We can also use the index() method to get the index of the first occurrence of an element in the list. For example, my_array.index(4) will return the index of the first occurrence of the number 4 in the list.
index_of_4 = my_array.index(4)
print(index_of_4) #Output- 2

#11.The range() is also used in the  list comprehension to create a list of numbers.
squares = [x**2 for x in range(10)]
print(squares)
#Output-
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#12.Looping through a list using range() function-
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(my_list)):
    print(my_list[i])
#Output-
#1
#2
#3
#4
#5
#6
#7
#8
#9
#10

#explanation-
#In the above code, we have created a list of numbers from 1 to 10. We have then used the range() function to loop through the list using the index of the elements. The range(len(my_list)) will return a range object that contains the indices of the elements in the list. We can then use these indices to access the elements of the list and print them.

#There are some array method which you learned before 

#1.appeend() method
#2.clear() method
#3.copy() method
#4.count() method
#5.extend() method
#6.index() method
#7.insert() method
#8.pop() method
#9.remove() method
#10.reverse() method
#11.sort() method
