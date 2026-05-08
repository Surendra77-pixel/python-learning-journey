
#                File handling in Python


#File handling is a crucial aspect of programming that allows us to read from and write to files. In Python, we can use built-in functions to perform various file operations such as opening, reading, writing, and closing files.

#In the real-life example - 

#1.data stores permenently in files, which can be accessed and manipulated using file handling techniques.

#2.read saved data later

#3.update information in files

#4.create reports and logs

#5.create reports and logs

#6.save logs 

#7.process huge data sets - this is where the file handling is used 

#File handling is the process of creating , reading , writing , updating and deleting files using programming languages. It allows us to store and manipulate data in a structured way, making it easier to manage and access information. In Python, we can use built-in functions to perform various file operations such as opening, reading, writing, and closing files.

#Without the file handling the data will be lost when the program ends. By using file handling techniques, we can ensure that our data is stored securely and can be accessed whenever needed. It also allows us to automate tasks such as data processing and report generation, making our programs more efficient and effective. Overall, file handling is an essential part of programming that enables us to work with data in a meaningful way.

#example in the bank sector -

#when you deposits money in the bank your balance will be updated in the files and the database due to files handling if the file handling is not there then the balance will not be updated and the data will be lost when the program ends. By using file handling techniques, we can ensure that our data is stored securely and can be accessed whenever needed. It also allows us to automate tasks such as data processing and report generation, making our programs more efficient and effective. Overall, file handling is an essential part of programming that enables us to work with data in a meaningful way.

#2.whatsapp back up - when you backup your whatsapp data it is stored in files and the database due to files handling if the file handling is not there then the data will be lost when the program ends. By using file handling techniques, we can ensure that our data is stored securely and can be accessed whenever needed. It also allows us to automate tasks such as data processing and report generation, making our programs more efficient and effective. Overall, file handling is an essential part of programming that enables us to work with data in a meaningful way.

#3.student management system - when you add a student in the student management system the data will be stored in files and the database due to files handling if the file handling is not there then the data will be lost when the program ends. By using file handling techniques, we can ensure that our data is stored securely and can be accessed whenever needed. It also allows us to automate tasks such as data processing and report generation, making our programs more efficient and effective. Overall, file handling is an essential part of programming that enables us to work with data in a meaningful way.

#4.instagram - when you post a photo on instagram the data will be stored in files and the database due to files handling if the file handling is not there then the data will be lost when the program ends. By using file handling techniques, we can ensure that our data is stored securely and can be accessed whenever needed. It also allows us to automate tasks such as data processing and report generation, making our programs more efficient and effective. Overall, file handling is an essential part of programming that enables us to work with data in a meaningful way.

#There are two types of file handling in python -

#1.text file handling - it is used to store and manipulate text data. It allows us to read and write text files, which can be used for various purposes such as storing configuration settings, logging information, and creating reports. 
#example - .txt, .csv, .json, .xml

#2.binary file handling - it is used to store and manipulate binary data. It allows us to read and write binary files, which can be used for various purposes such as storing images, videos, and audio files.
#example - .jpg, .png, .mp4, .mp3

#There are many file handling operations in python such as -

#1.opening a file -

#  it is used to open a file for reading or writing. It takes the file name and mode as arguments and returns a file object.
#example - open("file.txt", "r") - it opens the file in read mode


#2.reading a file -

#  it is used to read the contents of a file. It can be done using various methods such as read(), readline(), and readlines().
#example - file.read() - it reads the entire contents of the file


#3.writing to a file -

#  it is used to write data to a file. It can be done using various methods such as write() and writelines().
#example - file.write("Hello World") - it writes the string "Hello World" to the file


#4.appending to a file -

#  it is used to add data to the end of a file without overwriting the existing data. It can be done using the append mode ("a") when opening the file.
#example - open("file.txt", "a") - it opens the file in append mode

#5.updating a file -

#  it is used to modify the contents of a file. It can be done by reading the file, making the necessary changes, and then writing the updated content back to the file.


#6.deleting a file -

#  it is used to remove a file from the file system. It can be done using the os module in Python.
#example - os.remove("file.txt") - it deletes the file named "file.txt"


#7.renaming a file -

#  it is used to change the name of a file. It can be done using the os module in Python.
#example - os.rename("old_file.txt", "new_file.txt") - it renames the file "old_file.txt" to "new_file.txt"

#8.closing a file -

#  it is used to close a file after performing the necessary operations. It is important to close a file to free up system resources and ensure that any changes made to the file are saved properly.
#example - file.close() - it closes the file object

#9.with statement -

#  it is used to handle files in a more efficient way. It ensures that the file is properly closed after its suite finishes, even if an exception is raised. It is a recommended way to handle files in Python.
#example - with open("file.txt", "r") as file: - it opens the file in read mode and ensures that it is properly closed after the block of code is executed


#10.file handling is important in programming because it allows us to store and manipulate data in a structured way, making it easier to manage and access information. It also allows us to automate tasks such as data processing and report generation, making our programs more efficient and effective. Overall, file handling is an essential part of programming that enables us to work with data in a meaningful way.

# now let us now the short forms(modes) of file handling -

#1.r - it is used to open a file for reading. If the file does not exist, it will raise a FileNotFoundError.

#2.w - it is used to open a file for writing. If the file already exists, it will be overwritten. If the file does not exist, it will be created.

#3.a - it is used to open a file for appending. If the file already exists, the new data will be added to the end of the file. If the file does not exist, it will be created.

#4.x - it is used to open a file for exclusive creation. If the file already exists, it will raise a FileExistsError. If the file does not exist, it will be created.

#5.b - it is used to open a file in binary mode. It can be used in combination with other modes such as "rb" for reading a binary file and "wb" for writing to a binary file.

#6.t - it is used to open a file in text mode. It is the default mode and can be used in combination with other modes such as "rt" for reading a text file and "wt" for writing to a text file.

#7.+ - it is used to open a file for updating (reading and writing). It can be used in combination with other modes such as "r+" for reading and writing to a file, "w+" for writing and reading to a file (overwriting the existing file), and "a+" for appending and reading to a file.

#8.r+ - it is used to open a file for reading and writing. If the file does not exist, it will raise a FileNotFoundError.

#9.w+ - it is used to open a file for writing and reading. If the file already exists, it will be overwritten. If the file does not exist, it will be created.

#10.a+ - it is used to open a file for appending and reading. If the file already exists, the new data will be added to the end of the file. If the file does not exist, it will be created.

#11.x+ - it is used to open a file for exclusive creation and reading. If the file already exists, it will raise a FileExistsError. If the file does not exist, it will be created.

#12.t+ - it is used to open a file in text mode for reading and writing. It is the default mode and can be used in combination with other modes such as "rt+" for reading and writing to a text file, "wt+" for writing and reading to a text file (overwriting the existing file), and "at+" for appending and reading to a text file.

#13.b+ - it is used to open a file in binary mode for reading and writing. It can be used in combination with other modes such as "rb+" for reading and writing to a binary file, "wb+" for writing and reading to a binary file (overwriting the existing file), and "ab+" for appending and reading to a binary file.

#14.rb - it is used to open a file for reading in binary mode. If the file does not exist, it will raise a FileNotFoundError.

#15.wb - it is used to open a file for writing in binary mode. If the file already exists, it will be overwritten. If the file does not exist, it will be created.

#16.ab - it is used to open a file for appending in binary mode. If the file already exists, the new data will be added to the end of the file. If the file does not exist, it will be created.



#sample code for file handling in python -

# opening a file for writing

file = open("example.txt", "w")
file.write("Hello, this is an example of file handling in Python.")
file.close()

# opening a file for reading

file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# using with statement for file handling

with open("example.txt", "r") as file:
    content = file.read()
    print(content)  
    