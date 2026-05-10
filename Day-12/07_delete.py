
                                 #Deleting a file in Python

# To delete means removing a file or deleting its content from the file system. In Python, you can use the os module to delete a file. The os.remove() function is used to delete a file by specifying its path.

#There are two ways to delete a file in Python:

#1.Delete file content -

# To delete the content of a file, you can open the file in write mode ('w') and then close it immediately. This will effectively clear the content of the file while keeping the file itself intact.

file = open("demo.txt", "w")
file.close()
# In this example, we open "demo.txt" in write mode, which will overwrite the existing content of the file with an empty string. After closing the file, "demo.txt" will still exist but will be empty.

#2.Delete the entire file -

# To delete an entire file, you can use the os.remove() function from the os module. This will permanently remove the file from the file system

import os
os.remove("demo.txt")
# In this example, we import the os module and then call os.remove() with the name of the file we want to delete ("demo.txt"). This will permanently delete "demo.txt" from the file system. Be cautious when using os.remove(), as it will permanently delete the file and its content, and it cannot be undone.

#write mode can clear the content of a file, but it does not delete the file itself. The file will still exist on the file system, but it will be empty. If you want to completely remove the file from the file system, you need to use os.remove() or a similar method to delete the file.for example:

file = open("demo.txt", "w")  # This will clear the content of demo.txt but the file will still exist.
file.close()


file = open("demo.txt", "w")
file.write("Python")
file.close()
#output: Python


#Delete folder- 

import os
os.rmdir("folder_name")  # This will delete the folder named "folder_name". Note that the folder must be empty before it can be deleted. If the folder contains files or other folders, you will need to delete those first before deleting the folder itself.

