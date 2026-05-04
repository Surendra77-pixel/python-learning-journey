
#checking an item in a set - we can check if an item is present in a set using the in keyword. Here is an example:

#1.in operator -
#  we can use the in keyword to check if an item exists in a set. The in keyword returns True if the item is found in the set and False otherwise. Here is an example:
my_set = {"apple", "banana", "cherry"}
print("banana" in my_set) #output: True - The in keyword checks if the item "banana" is present in the set my_set and returns True because it is found in the set.
print("grape" in my_set) #output: False - The in keyword checks if the item "grape" is present in the set my_set and returns False because it is not found in the set.

#2.not in
my_set = {"apple", "banana", "cherry"}
print("grape" not in my_set) #output: True - The not in keyword checks if the item "grape" is not present in the set my_set and returns True because it is not found in the set.
print("banana" not in my_set) #output: False - The not in keyword checks if the item "banana" is not present in the set my_set and returns False because it is found in the set.

#3. using the if statement -

#  we can also use an if statement to check if an item is present in a set. Here is an example:
my_set = {"apple", "banana", "cherry"}
if "banana" in my_set:
    print("Item 'banana' is present in the set.") #output: Item 'banana' is present in the set. - The if statement checks if the item "banana" is present in the set my_set using the in keyword, and since it is found, it executes the print statement.   
if "grape" in my_set:
    print("Item 'grape' is present in the set.")
else:
    print("Item 'grape' is not present in the set.") #output: Item 'grape' is not present in the set. - The if statement checks if the item "grape" is present in the set my_set using the in keyword, and since it is not found, it executes the else block and prints a message indicating that the item is not present in the set.
    

