
#there are two ways to add the items in a tuple:

#1.convert into list and then back to tuple -

#  we can convert the tuple to a list, add the new item to the list, and then convert it back to a tuple. Here is an example:
my_tuple = (1, "hello", 3.14, True)
my_list = list(my_tuple)
my_list.append("new item")  # type: ignore
updated_tuple = tuple(my_list)
print(updated_tuple) #output: (1, 'hello', 3.14, True, 'new item') - The original tuple my_tuple is converted to a list my_list, the new item "new item" is added to the list using the append() method, and then the updated list is converted back to a tuple updated_tuple, resulting in (1, 'hello', 3.14, True, 'new item').   


#2.add tuple + tuple - we can create a new tuple by concatenating the existing tuple with another tuple that contains the new item. Here is an example:

my_tuple = (1, "hello", 3.14, True)
new_tuple = my_tuple + ("new item",)
print(new_tuple) #output: (1, 'hello', 3.14, True, 'new item') - The new_tuple contains all the elements of the original tuple my_tuple followed by the new element "new item", resulting in (1, 'hello', 3.14, True, 'new item').  

tuple=("Surendra","manthri","20","hyderabad")
y="new item"
tuple +=y # type: ignore
print(tuple) #output: ('Surendra', 'manthri', '20', 'hyderabad', 'new item') - The original tuple is concatenated with a tuple containing the string y, resulting in ('Surendra', 'manthri', '20', 'hyderabad', 'new item').

