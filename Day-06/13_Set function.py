
#set function -

# the set() function is used to create a set in Python. A set is an unordered collection of unique items. The set() function can take an iterable (such as a list, tuple, or another set) as an argument and returns a new set containing the unique elements from that iterable. Here is an example:

my_list = [1, 2, 3, 4, 5]
my_set = set(my_list)
print(my_set) #output: {1, 2, 3, 4, 5} - The set my_set is created by converting the list my_list using the set() function. The resulting set contains all the unique elements from the list, and since sets do not maintain order, the output may appear in a different order than the original list.

my_list = ["apple", "banana", "cherry", "apple"]
print(set(list(my_list))) #output: {'apple', 'banana', 'cherry'} - The set is created by converting the list my_list using the set() function. Since sets do not allow duplicate values, the duplicate "apple" is removed, resulting in a set that contains only unique elements from the list. The order of the items in the set may appear random because sets are unordered collections. 

s=set("hello")
print(s) #output: {'h', 'e', 'l', 'o'} - The set s is created by converting the string "hello" using the set() function. The resulting set contains the unique characters from the string, which are 'h', 'e', 'l', and 'o'. Since sets do not maintain order, the output may appear in a different order than the original string. Note that the duplicate character 'l' is only included once in the set.

