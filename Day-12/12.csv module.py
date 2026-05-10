

#                     csv module

# The csv module in Python provides functionality to read from and write to CSV (Comma Separated Values) files. It allows you to easily handle CSV data, which is a common format for storing tabular data.

#The csv is known as the comma separated values 

#it stores the data in a tabular format, where each row represents a record and each column represents a field. The values in each row are separated by commas (or other delimiters), making it easy to read and write data in a structured way.

#The csv in python is used to read  and write and convert the data into the rows and coloumns and also to handle the csv files. It provides functions to read from and write to csv files, as well as to manipulate the data in memory.

#why the csv module is used in python? The csv module is used in Python to handle CSV files, which are a common format for storing and exchanging tabular data. It provides functions to read from and write to CSV files, making it easy to work with structured data. The csv module allows you to easily parse CSV files, extract data, and manipulate it in memory. It also provides options for handling different delimiters, quoting characters, and other aspects of CSV formatting. Overall, the csv module simplifies the process of working with CSV data in Python.

#real time examples of using the csv module in python-

#1.student records
#2. employee data
#3. sales data
#4.Ai datset files 


#There are two main classes in the csv module for working with CSV files:

#1.csv.reader - This class is used to read data from a CSV file. It takes a file object as input and returns an iterator that produces each row of the CSV file as a list of strings. Example:

import csv
with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is printed as a list of strings.
#explanation: In this example, we open a CSV file named example.csv in read mode. We create a csv.reader object that reads from the file, and we iterate over each row produced by the reader. Each row is printed as a list of strings, where each string represents a field in the CSV file.

#2.csv.writer - This class is used to write data to a CSV file. It takes a file object as input and provides methods to write rows of data to the file. Example:

import csv
with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])  # Write a header row to the CSV file.
    writer.writerow(['Alice', 25, 'Los Angeles'])  # Write a data row to the CSV file.
    writer.writerow(['Bob', 30, 'New York'])  # Write another data row to the CSV file.
#output: A file named example.csv will be created (or overwritten if it already exists) with the following content:
#Name,Age,City
#Alice,25,Los Angeles
#Bob,30,New York
#explanation: In this example, we open a CSV file named example.csv in write mode. We create a csv.writer object that writes to the file, and we use the writerow() method to write rows of data to the CSV file. The first row is a header row that contains the field names, and the subsequent rows contain the data for each record. The newline='' argument in the open() function is used to prevent adding extra newlines between rows in the CSV file on some platforms.


#1.csv.dictreader - This class is used to read data from a CSV file and return each row as a dictionary, where the keys are the field names from the header row. Example:

import csv
with open('example.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)  # Each row is printed as a dictionary with field names as keys. 
#output: Each row of the CSV file will be printed as a dictionary. For example:
#{'Name': 'Alice', 'Age': '25', 'City': 'Los Angeles'}
#{'Name': 'Bob', 'Age': '30', 'City': 'New York'}
#explanation: In this example, we open a CSV file named example.csv in read mode. We create a csv.DictReader object that reads from the file, and we iterate over each row produced by the reader. Each row is printed as a dictionary, where the keys are the field names from the header row of the CSV file, and the values are the corresponding data for each record.

#2.csv.dictwriter - This class is used to write data to a CSV file using dictionaries, where the keys are the field names. Example:

import csv
with open('example.csv', 'w', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()  # Write the header row to the CSV file.
    writer.writerow({'Name': 'Alice', 'Age': 25, 'City': 'Los Angeles'})  # Write a data row to the CSV file using a dictionary.
    writer.writerow({'Name': 'Bob', 'Age': 30, 'City': 'New York'})  # Write another data row to the CSV file using a dictionary.
#output: A file named example.csv will be created (or overwritten if it already exists) with the following content:
#Name,Age,City
#Alice,25,Los Angeles
#Bob,30,New York
#explanation: In this example, we open a CSV file named example.csv in write mode. We define the field names for the CSV file and create a csv.DictWriter object that writes to the file. We use the writeheader() method to write the header row to the CSV file, and we use the writerow() method to write data rows to the CSV file using dictionaries. Each dictionary represents a record, where the keys are the field names and the values are the corresponding data for each record.

#The difference between csv.reader and csv.DictReader is that csv.reader returns each row as a list of strings, while csv.DictReader returns each row as a dictionary with field names as keys. Similarly, the difference between csv.writer and csv.DictWriter is that csv.writer writes rows of data as lists of values, while csv.DictWriter writes rows of data using dictionaries with field names as keys. The choice between these classes depends on how you want to work with the CSV data in your Python code.    

#The difference between csv.writer and csv.DictWriter is that csv.writer writes rows of data as lists of values, while csv.DictWriter writes rows of data using dictionaries with field names as keys. The choice between these classes depends on how you want to work with the CSV data in your Python code. If you prefer to work with lists of values, you can use csv.writer. If you prefer to work with dictionaries that have field names as keys, you can use csv.DictWriter. Both classes provide methods for writing data to a CSV file, but they differ in how the data is structured and accessed in your code.

