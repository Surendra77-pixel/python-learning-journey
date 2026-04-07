# looping the sets - we can loop through the items in a set using a for loop. Here is an example:

my_set = {"apple", "banana", "cherry"}
for item in my_set:
    print(item) #output: 'apple', 'banana', 'cherry' (order may vary) - The for loop iterates through each item in the set my_set and prints it. Since sets are unordered collections, the order of the items printed may vary each time you run the code.  

# we can also use a while loop to loop through the items in a set. Here is an example:
my_set = {"apple", "banana", "cherry"}
my_set_list = list(my_set) # Convert the set to a list to access items by index
index = 0
while index < len(my_set_list):
    print(my_set_list[index])
    index += 1  #output: 'apple', 'banana', 'cherry' (order may vary) - The while loop uses an index to access each item in the list created from the set my_set. Since sets are unordered, the order of the items printed may vary each time you run the code. After printing an item, the index is incremented to move to the next item until all items have been printed.
    
     
    