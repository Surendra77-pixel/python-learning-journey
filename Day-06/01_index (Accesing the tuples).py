
# accesing the tuples - You can access the elements of a tuple using indexing

#The example below demonstrates how to access individual elements of a tuple using both positive and negative indexing, as well as how to search for an element's index using the index() method-

my_tuplee = ("audi","mustang","ford","ferrari","bmw")
print(my_tuplee[0])
print(my_tuplee[1])
print(my_tuplee[2])
print(my_tuplee[3])
print(my_tuplee[4])
print(my_tuplee[-1])
print(my_tuplee[-2])
print(my_tuplee[-3])

    


#searching with the index and with position -

print(my_tuplee.index("ford")) #output: 2 - The index() method is used to find the index of the first occurrence of the item "ford" in the tuple my_tuplee. Since "ford" is found at index 2, the method returns 2 as the output.
