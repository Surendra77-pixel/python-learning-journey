
#                           append() 

#Adding new data at the end of an existing file without deleting old data.

#specifed the mode as 'a' to append to a file. If the file does not exist, it will create a new file. If the file already exists, it will add the new content to the end of the file without overwriting the existing content.


# To append to a file in Python, you can use the open() function with the 'a' mode. This allows you to add new content to the end of the file without overwriting the existing content. Here's how you can do it:

# Example of appending to a file using 'a' mode

with open('example.txt', 'a') as file:
    file.write('This line will be appended to the file.\n')  # Appends a line of text to the end of the file.

# You can also append multiple lines to a file at once by using the writelines() method, which takes a list of strings as an argument. For example:

lines_to_append = ['Fourth line.\n', 'Fifth line.\n', 'Sixth line.\n']
with open('example.txt', 'a') as file:
    file.writelines(lines_to_append)  # Appends multiple lines to the end of the file at once.
# When appending to a file, it's important to handle exceptions that may occur, such as IOError. You can use a try-except block to catch these exceptions and handle them gracefully. For example:

#example-

file = open("demo.txt", "a")
file.write(" Python")
file.close()

#The append and write is used to write the existing file. The difference is that append will add to the end of the file, while write will overwrite the existing content. If you want to keep the existing content and add new content to the end of the file, you should use append mode ('a'). If you want to replace the existing content with new content, you should use write mode ('w').

