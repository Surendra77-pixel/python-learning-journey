
#adding items to a set - 

# 1. add() method

#  we can add items to a set using the add() method. Here is an example:
my_set = {"apple", "banana", "cherry"}
my_set.add("date")
print(my_set) #output: {'apple', 'banana', 'cherry', 'date'} - The add() method adds the item "date" to the set my_set. Since sets do not allow duplicate values, if we try to add an item that already exists in the set, it will not be added again. For example:
my_set.add("banana")
print(my_set) #output: {'apple', 'banana', 'cherry', 'date'} - The add() method is called again to add the item "banana" to the set my_set. However, since "banana" is already present in the set, it will not be added again, and the set remains unchanged with the same elements.    


#2.update- 
#  we can add multiple items to a set using the update() method. The update() method takes an iterable (such as a list, tuple, or another set) as an argument and adds all the items from that iterable to the set. Here is an example:
my_set = {"apple", "banana", "cherry"}
my_set2= {"date", "elderberry", "fig"}
my_set.update(my_set2)
print(my_set) #output: {'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig'} - The update() method adds all the items from my_set2 to my_set. Since sets do not allow duplicate values, if any of the items in my_set2 were already present in my_set, they would not be added again. In this case, all the items in my_set2 are unique, so they are all added to my_set, resulting in a set that contains all the unique elements from both sets. 

#note - The object in the update method can be any iterable, such as a list, tuple, or another set. For example:
my_set = {"apple", "banana", "cherry"}
my_list = ["date", "elderberry", "fig"]
my_set.update(my_list)
print(my_set) #output: {'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig'} - The update() method adds all the items from the list my_list to the set my_set. Since sets do not allow duplicate values, if any of the items in my_list were already present in my_set, they would not be added again. In this case, all the items in my_list are unique, so they are all added to my_set, resulting in a set that contains all the unique elements from both the original set and the list.




