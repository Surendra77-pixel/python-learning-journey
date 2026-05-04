
#                       Os module in Python

#The os module in Python provides a way to interact with the operating system. It allows you to perform various tasks such as creating, deleting, and manipulating files and directories, as well as accessing environment variables and executing system commands. The os module is part of the Python standard library, so you can use it without having to install any additional packages.

#Some common functions provided by the os module include:

#1.import the os module-:

#To use the os module, you need to import it at the beginning of your Python script. This allows you to access the functions and variables defined in the os module.
import os

#2.Creating a directory:

#You can use the os.mkdir() function to create a new directory. For example, os.mkdir("my_directory") will create a directory named "my_directory" in the current working directory.
os.mkdir("my_directory")

#3.changing the current directory:

#You can use the os.chdir() function to change the current working directory. For example, os.chdir("my_directory") will change the current working directory to "my_directory".

os.chdir("my_directory")


#4.getting the current directory:

#You can use the os.getcwd() function to get the current working directory. For example, os.getcwd() will return the path of the current working directory as a string.

current_directory = os.getcwd()


#5.listing files and directories:

#You can use the os.listdir() function to get a list of files and directories in a specified path. For example, os.listdir(".") will return a list of files and directories in the current working directory.

files_and_directories = os.listdir(".")

#6.deleting a directory:

#You can use the os.rmdir() function to delete an empty directory. For example, os.rmdir("my_directory") will delete the directory named "my_directory" if it is empty.

os.rmdir("my_directory")

#7.deleting a file:

#You can use the os.remove() function to delete a file. For example, os.remove("my_file.txt") will delete the file named "my_file.txt".

os.remove("my_file.txt")

#8.renaming a file or directory:

#You can use the os.rename() function to rename a file or directory. For example, os.rename("old_name.txt", "new_name.txt") will rename the file "old_name.txt" to "new_name.txt".

os.rename("old_name.txt", "new_name.txt")

#9.checking if a file or directory exists:

#You can use the os.path.exists() function to check if a file or directory exists. For example, os.path.exists("my_file.txt") will return True if the file "my_file.txt" exists, and False otherwise.

file_exists = os.path.exists("my_file.txt")

#10.getting the size of a file:

#You can use the os.path.getsize() function to get the size of a file in bytes. For example, os.path.getsize("my_file.txt") will return the size of the file "my_file.txt" in bytes.

file_size = os.path.getsize("my_file.txt")

#11.getting the absolute path of a file or directory:

#You can use the os.path.abspath() function to get the absolute path of a file or directory. For example, os.path.abspath("my_file.txt") will return the absolute path of the file "my_file.txt".

absolute_path = os.path.abspath("my_file.txt")

#12.getting the file extension:

#You can use the os.path.splitext() function to get the file extension of a file. For example, os.path.splitext("my_file.txt") will return a tuple containing the file name and the file extension, which in this case would be ("my_file", ".txt").

file_name, file_extension = os.path.splitext("my_file.txt")

