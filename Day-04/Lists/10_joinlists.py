
#join lists:

#1. using the + operator - You can use the + operator to concatenate two lists, which creates a new list that contains all the items from both lists.
list1 = [1, 2, 3]   
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list) #output: [1, 2, 3, 4, 5, 6]

#2. using the extend() method - The extend() method is used to add all the items from one list to the end of another list. It modifies the original list in place.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1) #output: [1, 2, 3, 4, 5, 6]

#3. using the unpacking operator - You can also use the unpacking operator (*) to unpack the items from both lists into a new list.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = [*list1, *list2]
print(combined_list) #output: [1, 2, 3, 4, 5, 6]

#4. using the itertools.chain() function - The itertools.chain() function from the itertools module can be used to create an iterator that returns elements from the first list until it is exhausted, then returns elements from the second list.
import itertools
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list(itertools.chain(list1, list2))
print(combined_list) #output: [1, 2, 3, 4, 5, 6]

#5.using into 
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = [*list1, *list2]
print(combined_list) #output: [1, 2, 3, 4, 5, 6]

#6.using int0 -
list1 = [1, 2, 3]
list2 = [4, 5, 6]
for x in list2:
    list1.append(x) 
print(list1) #output: [1, 2, 3, 4, 5, 6]

