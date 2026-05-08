
#                     File Methods

# In Python, there are several methods available for working with files. Here are some commonly used file methods:

# open() - This method is used to open a file and returns a file object. It takes two arguments: the name of the file and the mode in which you want to open the file (e.g., 'r' for read, 'w' for write, 'a' for append).

# read() - This method is used to read the content of a file. It can be called on a file object returned by the open() method.

# write() - This method is used to write content to a file. It can be called on a file object returned by the open() method.

# close() - This method is used to close a file. It is important to close a file after you are done working with it to free up system resources.

#append() - This is not a method but a mode used with the open() function to specify that you want to append to a file rather than overwrite it.

#update() - This is not a built-in method for file handling in Python, but it can refer to the process of updating the content of a file by reading its current content, modifying it, and then writing the updated content back to the file.

#delete() - This is not a built-in method for file handling in Python, but it can refer to the process of deleting a file or its content using methods like os.remove() for deleting files or opening a file in write mode ('w') to clear its content.

# These methods and modes are essential for performing various operations on files in Python, such as reading, writing, appending, updating, and deleting files. Always remember to handle files properly by closing them after use and using context managers (with statement) to ensure that resources are managed efficiently.

#1."r" - Read mode: This is the default mode. It allows you to read the contents of a file. If the file does not exist, it will raise a FileNotFoundError.

#2."w" - Write mode: This mode allows you to write to a file. If the file already exists, it will overwrite the existing content. If the file does not exist, it will create a new file.

#3."a" - Append mode: This mode allows you to add content to the end of a file without overwriting the existing content. If the file does not exist, it will create a new file.

#4."x" - Exclusive creation mode: This mode allows you to create a new file. If the file already exists, it will raise a FileExistsError.

#5."b" - Binary mode: This mode is used for reading or writing binary files (e.g., images, audio files). It can be combined with other modes (e.g., 'rb' for reading a binary file, 'wb' for writing a binary file).

#6."t" - Text mode: This is the default mode for text files. It can be combined with other modes (e.g., 'rt' for reading a text file, 'wt' for writing a text file).

# When working with files, it's important to choose the appropriate mode based on your needs (e.g., whether you want to read, write, or append to a file) and to handle exceptions that may occur (e.g., FileNotFoundError, IOError) to ensure that your program runs smoothly. Always remember to close the file after you're done working with it to free up system resources. Using the with statement is a good practice for managing files, as it ensures that the file is properly closed even if an error occurs.

#r+- Read text mode (default) why it is called default? because if you do not specify the mode when opening a file, it will default to 'r' (read mode) and 't' (text mode). This means that if you simply use open('example.txt'), it will be equivalent to open('example.txt', 'rt'), which is why 'rt' is considered the default mode for opening text files in Python.

#2.w+ - Write text mode: This mode allows you to write to a file. If the file already exists, it will overwrite the existing content. If the file does not exist, it will create a new file. When you open a file in 'wt' mode, you are telling Python that you want to write text to the file. If the file already has content, it will be replaced with the new content you write. If the file does not exist, it will be created and then you can write to it.

#3.a+ - Append text mode: This mode allows you to add content to the end of a file without overwriting the existing content. If the file does not exist, it will create a new file. When you open a file in 'at' mode, you are telling Python that you want to append text to the file. If the file already has content, your new content will be added to the end of the file rather than replacing it. If the file does not exist, it will be created and then you can append to it.


#4.rb - Read binary mode: This mode is used for reading binary files (e.g., images, audio files). When you open a file in 'rb' mode, you are telling Python that you want to read the file as binary data. This is important for non-text files, as it allows you to read the raw bytes of the file without any encoding or decoding.

#5.wb - Write binary mode: This mode is used for writing binary files (e.g., images, audio files). When you open a file in 'wb' mode, you are telling Python that you want to write binary data to the file. If the file already exists, it will overwrite the existing content. If the file does not exist, it will create a new file. When you write to a file in 'wb' mode, you need to provide the data as bytes


#6.xt - Exclusive creation text mode: This mode allows you to create a new file. If the file already exists, it will raise a FileExistsError. When you open a file in 'xt' mode, you are telling Python that you want to create a new text file. If the file already exists, it will not be overwritten and instead, a FileExistsError will be raised. If the file does not exist, it will be created and then you can write to it.

#7.t+ - Text mode for both reading and writing: This mode allows you to read and write to a file. If the file does not exist, it will create a new file. When you open a file in 't+' mode, you are telling Python that you want to read and write text to the file. If the file already exists, you can read from it and also write to it without overwriting the existing content. If the file does not exist, it will be created and then you can read from and write to it.

#8.b+ - Binary mode for both reading and writing: This mode allows you to read and write to a binary file. If the file does not exist, it will create a new file. When you open a file in 'b+' mode, you are telling Python that you want to read and write binary data to the file. If the file already exists, you can read from it and also write to it without overwriting the existing content. If the file does not exist, it will be created and then you can read from and write to it as binary data.

#9.rb - Read binary mode: This mode is used for reading binary files (e.g., images, audio files). When you open a file in 'rb' mode, you are telling Python that you want to read the file as binary data. This is important for non-text files, as it allows you to read the raw bytes of the file without any encoding or decoding.


#10.wb - Write binary mode: This mode is used for writing binary files (e.g., images, audio files). When you open a file in 'wb' mode, you are telling Python that you want to write binary data to the file. If the file already exists, it will overwrite the existing content. If the file does not exist, it will create a new file. When you write to a file in 'wb' mode, you need to provide the data as bytes.

#11.ab - Append binary mode: This mode allows you to add content to the end of a binary file without overwriting the existing content. If the file does not exist, it will create a new file. When you open a file in 'ab' mode, you are telling Python that you want to append binary data to the file. If the file already has content, your new content will be added to the end of the file rather than replacing it. If the file does not exist, it will be created and then you can append to it as binary data.

