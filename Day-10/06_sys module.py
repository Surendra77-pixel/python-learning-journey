
#                          SYS MODULE IN PYTHON

#The sys module in Python provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is a built-in module that is always available in Python.

#Some common functions and variables provided by the sys module include:

#1.argv:

#The sys.argv list contains the command-line arguments passed to a Python script. The first element of the list is the name of the script itself, followed by any additional arguments. For example, if you run a script with the command python script.py arg1 arg2, sys.argv will be ['script.py', 'arg1', 'arg2'].

import sys
print(sys.argv) #Output- ['script.py', 'arg1', 'arg2']


#2.exit():

#The sys.exit() function is used to exit from a Python script. It can be called with an optional argument that specifies the exit status. For example, sys.exit(0) will exit the script with a status of 0, which typically indicates successful completion.

import sys
sys.exit(0) #This will exit the script with a status of 0

#3.maxsize:

#The sys.maxsize variable represents the largest positive integer that can be used in Python. It is typically used to determine the maximum size of data structures or to check for overflow conditions. For example, sys.maxsize will return a large integer value that represents the maximum size of a list or other data structure.

import sys
print(sys.maxsize) #Output- 9223372036854775807 (on a 64-bit system)

#4.path:

#The sys.path list contains the directories that the Python interpreter searches for modules when you import them. It includes the current working directory, as well as any directories specified in the PYTHONPATH environment variable. For example, sys.path will return a list of directories that the interpreter will search for modules.

import sys
print(sys.path) #Output- A list of directories that the interpreter will search for modules

#5.version:

#The sys.version variable contains a string that represents the version of Python that is currently being used. It includes information about the major, minor, and micro versions of Python, as well as any additional information about the build or platform. For example, sys.version will return a string that represents the version of Python being used.

import sys
print(sys.version) #Output- A string that represents the version of Python being used

