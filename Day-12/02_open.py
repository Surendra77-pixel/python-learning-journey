
#         open()

#The open() function is used to open a file in Python. It takes two arguments: the name of the file and the mode in which to open it (e.g., 'r' for read, 'w' for write, 'a' for append). The function returns a file object that can be used to read from or write to the file.

# Example of opening a file for reading

file = open('example.txt', 'r')

# Example of opening a file for writing

file = open('example.txt', 'w')

# Example of opening a file for appending

file = open('example.txt', 'a')

# After opening a file, it's important to close it using the close() method to free up system resources.

file.close()


## In summary, the open() function is essential for working with files in Python, allowing you to read, write, or append data to files as needed. Always remember to close the file after you're done to ensure proper resource management.

## Note: When using the open() function, it's a good practice to use a context manager (the with statement) to ensure that the file is properly closed even if an error occurs.for example:

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)  

#What is the with statement in Python?

#The with statement in Python is used to wrap the execution of a block of code within methods defined by a context manager. It is commonly used for managing resources such as file streams, ensuring that they are properly acquired and released. When you use the with statement, it automatically takes care of closing the file or releasing any resources, even if an error occurs within the block.

# Example of using the with statement to open a file

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)  # The file will be automatically closed after this block no matter what happens.when you are using the with statement, you don't need to explicitly call file.close() as it will be handled automatically. This makes your code cleaner and more robust.

#Without the mode argument, the open() function defaults to 'r' which is txt (read mode), which means it will try to read from the file. If the file does not exist, it will raise a FileNotFoundError. Always specify the mode when opening a file to avoid unexpected behavior

#If the file is in the different directory, you can provide the relative or absolute path to the file in the open() function. For example:

# Using a relative path - “Start searching from the current working folder.”

project/
│
├── main.py
└── subfolder/
    └── example.txt

with open('subfolder/example.txt', 'r') as file:
    content = file.read()
    print(content)

# Using an absolute path - An absolute path gives the complete file location from the root directory.

with open('/path/to/your/file/example.txt', 'r') as file:
    content = file.read()
    print(content)
 
C:/Users/Surendra/Documents/example.txt



 #         or

 f = open("D:\\myfiles\welcome.txt")
print(f.read()) 


#your windows path -

f = open("D:\\myfiles\welcome.txt")
print(f.read())