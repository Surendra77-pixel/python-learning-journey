

#                            create.py  

# To create a new file in Python, you can use the open() function with the 'w' mode. This will create a new file if it does not already exist. If the file already exists, it will overwrite the existing file. Here's how you can create a new file:

#python can create a file using 

#w mode - write mode - it will create a new file if it does not exist, or overwrite the existing file if it does exist.

#a mode - append mode - it will create a new file if it does not exist, or append to the end of the existing file if it does exist.

#x mode - exclusive creation mode - it will create a new file, but if the file already exists, it will raise a FileExistsError.

# Example of creating a new file using 'w' mode

file = open("demo.txt", "w")
file.close()
# In this example, we use the open() function with 'w' mode to create a new file named "demo.txt". If "demo.txt" already exists, it will be overwritten. After creating the file, we close it using the close() method.

#        or 

with open("demo.txt", "w") as file:
    pass  # This will create a new file named "demo.txt" and then immediately close it. The pass statement is used here as a placeholder since we don't need to write anything to the file at this point.

#a new file is named "demo.txt" is created and if the file already exists,old data will be deleted and new file will be created.


# Example of creating a new file using 'x' mode

file = open("demo.txt", "x")
file.close()
# In this example, we use the open() function with 'x' mode to create a new file named "demo.txt". If "demo.txt" already exists, it will raise a FileExistsError. After creating the file, we close it using the close() method.

#create a new file named "demo.txt" using 'x' mode. If "demo.txt" already exists, it will raise a FileExistsError.

#                 or

with open("demo.txt", "x") as file:
    pass  # This will create a new file named "demo.txt" and then immediately close it. If "demo.txt" already exists, it will raise a FileExistsError. The pass statement is used here as a placeholder since we don't need to write anything to the file at this point.

#example of creating a new file using 'a' mode

file = open("demo.txt", "a")
file.close()
# In this example, we use the open() function with 'a' mode to create a new file named "demo.txt". If "demo.txt" already exists, it will not overwrite the existing file but will allow you to append new content to it. After creating the file, we close it using the close() method.

#creates the file if it does not exist 
#keep old data if file already exists

