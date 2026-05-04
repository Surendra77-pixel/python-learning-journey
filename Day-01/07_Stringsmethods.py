
#string methods- the string methods are the built in functions which are used to perform the operations on the string there are few types of the string methods these are used in the strings to perform the operations on the string 

#1. upper() - 
# The upper() method is used to convert all the characters in a string to uppercase. It returns a new string with all characters in uppercase.
my_string = "Hello, World!" 
print(my_string.upper()) #output: "HELLO, WORLD!" - The upper() method converts all characters in the string to uppercase, resulting in "HELLO, WORLD!".


#2. lower() -
# The lower() method is used to convert all the characters in a string to lowercase. It returns a new string with all characters in lowercase.
my_string = "Hello, World!"
print(my_string.lower()) #output: "hello, world!" - The lower() method converts all characters in the string to lowercase, resulting in "hello, world!".


#3.capitalize() -
# The capitalize() method is used to convert the first character of a string to uppercase and the rest of the characters to lowercase. It returns a new string with the first character capitalized and the rest in lowercase.
my_string = "hello, world!"
print(my_string.capitalize()) #output: "Hello, world!" - The capitalize() method converts the first character of the string to uppercase and the rest to lowercase, resulting in "Hello, world!".


#4.title()- 
# The title() method is used to convert the first character of each word in a string to uppercase and the rest of the characters to lowercase. It returns a new string with the first character of each word capitalized and the rest in lowercase.
my_string = "hello, world!"
print(my_string.title()) #output: "Hello, World!" - The title() method converts the first character of each word in the string to uppercase and the rest to lowercase, resulting in "Hello, World!".


#5.strip() -
# The strip() method is used to remove any leading and trailing whitespace from a string. It returns a new string with the whitespace removed.
my_string = "   Hello, World!   "
print(my_string.strip()) #output: "Hello, World!" - The strip() method removes the leading and trailing whitespace from the string, resulting in "Hello, World!".


#6replace() -
# The replace() method is used to replace all occurrences of a specified substring with another substring.
my_string = "Hello, World!"
print(my_string.replace("World", "Python")) #output: "Hello, Python!" - The replace() method replaces all occurrences of the substring "World" with "Python", resulting in "Hello, Python!".


#7.find() -
# The find() method is used to find the index of the first occurrence of a specified substring in a string. It returns the index of the first occurrence of the substring, or -1 if the substring is not found.
my_string = "Hello, World!"
print(my_string.find("World")) #output: 7 - The find() method returns the index of the first occurrence of the substring "World", which is 7 in this case.

print(my_string.find("Python")) #output: -1 - The find() method returns -1 because the substring "Python" is not found in the string "Hello, World!".


#8.split() -
# The split() method is used to split a string into a list of substrings based on a specified delimiter. It returns a list of substrings.
my_string = "Hello, World!"
print(my_string.split(", ")) #output: ['Hello', 'World!'] - The split() method splits the string into a list of substrings based on the delimiter ", ", resulting in ['Hello', 'World!'].


#9.startwith(prefix) -
# The startswith() method is used to check if a string starts with a specified prefix. It returns True if the string starts with the prefix, and False otherwise.
my_string = "Hello, World!"
print(my_string.startswith("Hello")) #output: True - The startswith() method returns True because the string "Hello, World!" starts with the prefix "Hello".

print(my_string.startswith("World")) #output: False - The startswith() method returns False because the string "Hello, World!" does not start with the prefix "World".    


#10.endswith(Suffix) -
# The endswith() method is used to check if a string ends with a specified suffix.
my_string = "Hello, World!"
print(my_string.endswith("World!")) #output: True - The endswith() method returns True because the string "Hello, World!" ends with the suffix "World!".

#11.count(substring) -
# The count() method is used to count the number of occurrences of a specified substring in a string. It returns the number of occurrences of the substring.
my_string = "Hello, World! Hello!"
print(my_string.count("Hello")) #output: 2 - The count() method returns the number of occurrences of the substring "Hello" in the string, which is 2 in this case.


#12.find((sub,start,end) -
# The find() method can also take optional start and end parameters to specify the range within the string to search for the substring. It returns the index of the first occurrence of the substring within the specified range, or -1 if the substring is not found.
my_string = "Hello, World! Hello!"
print(my_string.find("Hello", 5)) #output: 14 - The find() method searches for the substring "Hello" starting from index 5 and returns the index of the first occurrence, which is 14 in this case.


#13.find(substring)-
# The find() method is used to find the index of the first occurrence of a specified substring in a string. It returns the index of the first occurrence of the substring, or -1 if the substring is not found.
my_string = "Hello, World!"
print(my_string.find("World")) #output: 7 - The find() method returns the index of the first occurrence of the substring "World", which is 7 in this case.


#14.index(substring) -
# The index() method is similar to the find() method, but it raises a ValueError if the substring is not found instead of returning -1.
my_string = "Hello, World!"
print(my_string.index("World")) #output: 7 - The index() method returns the index of the first occurrence of the substring "World", which is 7 in this case.


#15.index(sub,standard,end) -
# The index() method can also take optional start and end parameters to specify the range within the string to search for the substring. It returns the index of the first occurrence of the substring within the specified range, or raises a ValueError if the substring is not found.
my_string = "Hello, World! Hello!"
print(my_string.index("Hello", 5)) #output: 14 - The index() method searches for the substring "Hello" starting from index 5 and returns the index of the first occurrence, which is 14 in this case.


#16.isnumeric() -
# The isnumeric() method is used to check if all characters in a string are numeric. It returns True if all characters in the string are numeric, and False otherwise.
my_string = "12345"
print(my_string.isnumeric()) #output: True - The isnumeric() method returns True because all characters in the string "12345" are numeric.


#17.isnumeric() -
# The isnumeric() method is used to check if all characters in a string are numeric. It returns True if all characters in the string are numeric, and False otherwise.
my_string = "12345"
print(my_string.isnumeric()) #output: True - The isnumeric() method returns True because all characters in the string "12345" are numeric.


#18.isalpha() -
# The isalpha() method is used to check if all characters in a string are alphabetic. It returns True if all characters in the string are alphabetic, and False otherwise.
my_string = "Hello"
print(my_string.isalpha()) #output: True - The isalpha() method returns True because all characters in the string "Hello" are alphabetic.


#19.isalnum() -
# The isalnum() method is used to check if all characters in a string are alphanumeric (i.e., either alphabetic or numeric). It returns True if all characters in the string are alphanumeric, and False otherwise.
my_string = "Hello123"
print(my_string.isalnum()) #output: True - The isalnum() method returns True because all characters in the string "Hello123" are alphanumeric (i.e., either alphabetic or numeric).


#20.isdigit() -
# The isdigit() method is used to check if all characters in a string are digits. It returns True if all characters in the string are digits, and False otherwise.
my_string = "12345"
print(my_string.isdigit()) #output: True - The isdigit() method returns True because all characters in the string "12345" are digits.


#21.islower() -
# The islower() method is used to check if all characters in a string are lowercase. It returns True if all characters in the string are lowercase, and False otherwise.
my_string = "hello" 
print(my_string.islower()) #output: True - The islower() method returns True because all characters in the string "hello" are lowercase.


#22.isupper() -
# The isupper() method is used to check if all characters in a string are uppercase. It returns True if all characters in the string are uppercase, and False otherwise.
my_string = "HELLO"
print(my_string.isupper()) #output: True - The isupper() method returns True because all characters in the string "HELLO" are uppercase.


#23.isacii() -
# The isascii() method is used to check if all characters in a string are ASCII characters. It returns True if all characters in the string are ASCII characters, and False otherwise.
my_string = "Hello"
print(my_string.isascii()) #output: True - The isascii() method returns True because all characters in the string "Hello" are ASCII characters.


#24.isprintable() -
# The isprintable() method is used to check if all characters in a string are printable. It returns True if all characters in the string are printable, and False otherwise.
my_string = "Hello"
print(my_string.isprintable()) #output: True - The isprintable() method returns True because all characters in the string "Hello" are printable.


#25.isspace() -
# The isspace() method is used to check if all characters in a string are whitespace characters. It returns True if all characters in the string are whitespace characters, and False otherwise.
my_string = "   "
print(my_string.isspace()) #output: True - The isspace() method returns True because all characters in the string "   " are whitespace characters.


#26.istitle() -
# The istitle() method is used to check if a string is in title case (i.e., the first character of each word is uppercase and the rest of the characters are lowercase). It returns True if the string is in title case, and False otherwise.
my_string = "Hello, World!"
print(my_string.istitle()) #output: True - The istitle() method returns True because the string "Hello, World!" is in title case (i.e., the first character of each word is uppercase and the rest of the characters are lowercase).


#27.isnumeric() -
# The isnumeric() method is used to check if all characters in a string are numeric. It returns True if all characters in the string are numeric, and False otherwise.
my_string = "12345"
print(my_string.isnumeric()) #output: True - The isnumeric() method returns True because all characters in the string "12345" are numeric.


#28.eval() -
# The eval() function is used to evaluate a string as a Python expression. It takes a string as input and returns the result of evaluating the string as a Python expression.
expression = "2 + 3 * 4"
result = eval(expression)
print(result) #output: 14 - The eval() function evaluates the string "2 + 3 * 4" as a Python expression and returns the result, which is 14 in this case.

i=eval(input("Enter the expression: "))
print(i) #output: (depends on the input) - The eval() function evaluates the user input as a Python expression and returns the result. The output will depend on the expression entered by the user.

#example input:2 + 3 * 4
#example output: 14 - The eval() function evaluates the expression "2 + 3 * 4" entered by the user and returns the result, which is 14 in this case.    






