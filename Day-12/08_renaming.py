
#                               Renaming

# changing the oild file name to new file name

#python used the os.rename() function to rename a file. The os.rename() function takes two arguments: the current name of the file and the new name you want to give it.

import os
os.rename("old_file_name", "new_file_name")

# In this example, replace "old_file_name" with the current name of the file you want to rename, and replace "new_file_name" with the new name you want to give the file. After running this code, the file will be renamed to the new name you specified.


#safe renaming-

import os
if os.path.exists("demo.txt"):
    os.rename("demo.txt", "newdemo.txt")
    print("File renamed")
else:
    print("File not found")
# In this example, we first check if the file "demo.txt" exists using os.path.exists(). If the file exists, we proceed to rename it to "newdemo.txt" using os.rename() and print a success message. If the file does not exist, we print a message indicating that the file was not found. This approach helps prevent errors that may occur if you try to rename a file that does not exist.


#os.rename() - rename a file 

#os.path.exists() - check if a file exists before renaming it to avoid errors.

