
#                     Dir Module and types of files


#The os module in Python provides a way to interact with the operating system, including working with directories and files. The os module provides several functions for working with directories and files, including:

#1.listdir():
#The os.listdir() function is used to list the contents of a directory. It takes a directory path as input and returns a list of the names of the files and directories in that directory. For example, you can use os.listdir() to list the contents of the current working directory:
import os   
current_directory = os.getcwd()  # Get the current working directory
contents = os.listdir(current_directory)  # List the contents of the current directory
print(contents) #Output- A list of the names of the files and directories in the current directory
#In the above code, we have imported the os module and used the getcwd() function to get the current working directory. We then pass the current directory path to the os.listdir() function, which returns a list of the names of the files and directories in that directory. The resulting list is then printed to the console.


#2.path.isfile() and path.isdir():
#The os.path.isfile() function is used to check if a given path is a file, while the os.path.isdir() function is used to check if a given path is a directory. Both functions take a path as input and return True if the path is a file or directory, respectively, and False otherwise. For example, you can use these functions to check if a specific path is a file or directory:
import os
path = 'example.txt'  # Replace with your file or directory path
if os.path.isfile(path):
    print(f"{path} is a file.")
elif os.path.isdir(path):
    print(f"{path} is a directory.")
else:
    print(f"{path} does not exist.")
#In the above code, we have imported the os module and defined a path variable that represents a file or directory path. We then use the os.path.isfile() function to check if the path is a file, and if it is, we print a message indicating that it is a file. If the path is not a file, we use the os.path.isdir() function to check if it is a directory, and if it is, we print a message indicating that it is a directory. If neither condition is true, we print a message indicating that the path does not exist.


#3.mkdir() and makedirs():
#The os.mkdir() function is used to create a new directory, while the os.makedirs() function is used to create a directory and any necessary parent directories. Both functions take a directory path as input and create the specified directory. For example, you can use these functions to create a new directory:
import os
new_directory = 'new_folder'  # Replace with your desired directory name
os.mkdir(new_directory)  # This will create a new directory called 'new_folder'
#In the above code, we have imported the os module and defined a new_directory variable that represents the name of the directory we want to create. We then use the os.mkdir() function to create a new directory with the specified name. If you want to create a directory along with any necessary parent directories, you can use os.makedirs() instead:

import os
new_directory = 'parent_folder/new_folder'  # Replace with your desired directory path
os.makedirs(new_directory)  # This will create the 'parent_folder' and 'new_folder' directories
#In the above code, we have defined a new_directory variable that represents a directory path that includes a parent directory and a child directory. We then use the os.makedirs() function to create both the parent directory and the child directory in one step. If the parent directory already exists, os.makedirs() will not raise an error and will simply create the child directory within it.


#4.remove() and rmdir():
#The os.remove() function is used to delete a file, while the os.rmdir() function is used to delete an empty directory. Both functions take a path as input and delete the specified file or directory. For example, you can use these functions to delete a file or an empty directory:
import os
file_to_delete = 'example.txt'  # Replace with your file path
os.remove(file_to_delete)  # This will delete the specified file
#In the above code, we have imported the os module and defined a file_to_delete variable that represents the path of the file we want to delete. We then use the os.remove() function to delete the specified file. If you want to delete an empty directory, you can use os.rmdir() instead:   
import os
directory_to_delete = 'empty_folder'  # Replace with your directory path
os.rmdir(directory_to_delete)  # This will delete the specified empty directory
#In the above code, we have defined a directory_to_delete variable that represents the path of the empty directory we want to delete. We then use the os.rmdir() function to delete the specified empty directory. Note that os.rmdir() will only work if the directory is empty; if it contains any files or subdirectories, you will need to use os.remove() to delete those contents before deleting the directory itself.


#5.rename():
#The os.rename() function is used to rename a file or directory. It takes two arguments: the current name of the file or directory and the new name. For example, you can use os.rename() to rename a file:
import os
current_name = 'old_name.txt'  # Replace with your current file name
new_name = 'new_name.txt'  # Replace with your desired new file name
os.rename(current_name, new_name)  # This will rename 'old_name.txt' to 'new_name.txt'
#In the above code, we have imported the os module and defined two variables: current_name, which represents the current name of the file we want to rename, and new_name, which represents the desired new name for the file. We then use the os.rename() function to rename the file from its current name to the new name specified. You can also use os.rename() to rename a directory in a similar way by providing the current and new directory names as arguments.

#Types of files:

#1. Regular files: These are the most common type of files that contain data, such as text files, binary files, images, and more. Regular files can be created, read, written to, and deleted using various file handling functions in Python.

#2. Directories: These are special types of files that can contain other files and directories. Directories are used to organize files in a hierarchical structure. You can create, list, and delete directories using functions from the os module in Python.

#3. Symbolic links: These are special types of files that act as pointers to other files or directories. Symbolic links allow you to create shortcuts or aliases to files and directories, making it easier to access them from different locations in the file system.

#4. Device files: These are special types of files that represent hardware devices, such as printers, scanners, and more. Device files allow you to interact with hardware devices using file handling functions in Python.

#5. Pipes: These are special types of files that allow for inter-process communication. Pipes can be used to send data between different processes running on the same machine, allowing them to communicate and share information.

