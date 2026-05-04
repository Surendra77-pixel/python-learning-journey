
#Converting list to set - 

# we can convert a list to a set using the set() function. Here is an example:

my_list = [1, 2, 3, 4, 5]
my_set = set(my_list)
print(my_set) #output: {1, 2, 3, 4, 5} - The set my_set is created by converting the list my_list using the set() function. The resulting set contains all the unique elements from the list, and since sets do not maintain order, the output may appear in a different order than the original list.  


my_list = ["apple", "banana", "cherry", "apple"]
print(set(list(my_list))) #output: {'apple', 'banana', 'cherry'} - The set is created by converting the list my_list using the set() function. Since sets do not allow duplicate values, the duplicate "apple" is removed, resulting in a set that contains only unique elements from the list. The order of the items in the set may appear random because sets are unordered collections.


