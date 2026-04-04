
#checking items in a list - You can check if an item exists in a list using the in keyword. The in keyword returns True if the item is found in the list and False if it is not found. The syntax for checking if an item exists in a list is item in list, where item is the value you want to check for and list is the list you want to check in.    


#1. checking if an item exists in a list - You can use the in keyword to check if an item exists in a list. The syntax for checking if an item exists in a list is item in list, where item is the value you want to check for and list is the list you want to check in.
fruits = ["apple", "banana", "cherry", "date", "fig"]
print("banana" in fruits) #output: True
print("grape" in fruits) #output: False


#2. checking if an item does not exist in a list - You can also use the not in keyword to check if an item does not exist in a list. The syntax for checking if an item does not exist in a list is item not in list, where item is the value you want to check for and list is the list you want to check in.
fruits = ["apple", "banana", "cherry", "date", "fig"]
print("grape" not in fruits) #output: True
print("banana" not in fruits) #output: False


#3. checking if an item exists in a list using a loop - You can also check if an item exists in a list by using a loop to iterate through the list and compare each item to the value you want to check for. The syntax for checking if an item exists in a list using a loop is:
item_exists = False
fruits = ["apple", "banana", "cherry", "date", "fig"]
for fruit in fruits:
    if fruit == "banana":
        item_exists = True
        break
print(item_exists) #output: True
#explanation: In this code, we initialize a variable item_exists to False. We then use a for loop to iterate through each item in the fruits list. If we find an item that matches "banana", we set item_exists to True and break out of the loop. Finally, we print the value of item_exists, which will be True if "banana" was found in the list and False otherwise.


#4 using .index() method to check if an item exists in a list - You can also use the .index() method to check if an item exists in a list. The .index() method returns the index of the first occurrence of the specified value in the list. If the value is not found, it raises a ValueError. The syntax for using the .index() method to check if an item exists in a list is:
fruits = ["apple", "banana", "mango"]
print(fruits.index("banana"))  # 1

#5.using .count() method to check if an item exists in a list - You can also use the .count() method to check if an item exists in a list. The .count() method returns the number of occurrences of the specified value in the list. If the value is not found, it returns 0. The syntax for using the .count() method to check if an item exists in a list is:
fruits = ["apple", "banana", "mango"]
print(fruits.count("banana"))  # 1


#real life example -
 
students = ["Ravi", "Priya", "Arun"]

name = input("Enter your name: ")

if name in students:
    print("Present ")
else:
    print("Absent ")
    #output:enter your name: Priya
    #Present


#checking item in a list takes 0(n) time complexity because in the worst case, we may have to check every item in the list to find the item we are looking for. If the item is not found, we will have to check all items in the list, resulting in a time complexity of O(n).\n is the number of items in the list.
my_set = {1, 2, 3, 4}
print(3 in my_set)  # Faster ⚡