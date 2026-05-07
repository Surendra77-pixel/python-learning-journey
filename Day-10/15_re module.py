

#                 re module in Python

#The re module in Python provides functions for working with regular expressions. Regular expressions are a powerful tool for searching and manipulating strings based on specific patterns. The re module allows you to perform various operations such as searching, matching, and replacing strings using regular expressions.

#Some common functions provided by the re module include:

#1.search():
#The re.search() function is used to search for a pattern in a string. It takes a regular expression pattern and a string as input and returns a match object if the pattern is found, or None if it is not found. For example, you can use re.search() to find the first occurrence of a word in a string:
import re
text = "Hello, my name is Alice."
match = re.search(r'\bAlice\b', text)
if match:
    print("Found:", match.group()) #Output- Found: Alice
#In the above code, we have imported the re module and defined a string called text. We then use the re.search() function to search for the word "Alice" in the text. The regular expression pattern r'\bAlice\b' ensures that we are searching for the whole word "Alice" and not just a substring. If a match is found, we print the matched word using match.group().

#2.match():
#The re.match() function is used to check if a pattern matches the beginning of a string. It takes a regular expression pattern and a string as input and returns a match object if the pattern matches the beginning of the string, or None if it does not match. For example, you can use re.match() to check if a string starts with a specific word:
import re
text = "Hello, my name is Alice."
match = re.match(r'Hello', text)
if match:
    print("Match found:", match.group()) #Output- Match found: Hello
#In the above code, we have used the re.match() function to check if the string text starts with the word "Hello". The regular expression pattern r'Hello' checks for a match at the beginning of the string. If a match is found, we print the matched word using match.group().


#3.findall():
#The re.findall() function is used to find all occurrences of a pattern in a string. It takes a regular expression pattern and a string as input and returns a list of all matches found in the string. For example, you can use re.findall() to find all the words in a string:
import re
text = "Hello, my name is Alice. I am learning Python."
words = re.findall(r'\b\w+\b', text)
print(words) #Output- ['Hello', 'my', 'name', 'is', 'Alice', 'I', 'am', 'learning', 'Python']
#In the above code, we have used the re.findall() function to find all the words in the string text. The regular expression pattern r'\b\w+\b' matches any sequence of word characters (letters, digits, or underscores) that are surrounded by word boundaries. The resulting list of words is then printed to the console.


#4.sub():
#The re.sub() function is used to replace occurrences of a pattern in a string with a specified replacement string. It takes a regular expression pattern, a replacement string, and a target string as input and returns a new string with the replacements made. For example, you can use re.sub() to replace all occurrences of a word in a string:
import re
text = "Hello, my name is Alice. Alice is learning Python."
new_text = re.sub(r'\bAlice\b', 'Bob', text)
print(new_text) #Output- Hello, my name is Bob. Bob is learning Python.
#In the above code, we have used the re.sub() function to replace all occurrences of the word "Alice" with "Bob" in the string text. The regular expression pattern r'\bAlice\b' ensures that we are replacing the whole word "Alice" and not just a substring. The resulting new_text string is then printed to the console, showing the replacements made.


#5.split():
#The re.split() function is used to split a string into a list of substrings based on a specified pattern. It takes a regular expression pattern and a string as input and returns a list of substrings that are separated by the pattern. For example, you can use re.split() to split a string into words based on whitespace:
import re
text = "Hello, my name is Alice."
words = re.split(r'\s+', text)
print(words) #Output- ['Hello,', 'my', 'name', 'is', 'Alice.']
#In the above code, we have used the re.split() function to split the string text into a list of words based on whitespace. The regular expression pattern r'\s+' matches one or more whitespace characters, which allows us to split the string into individual words. The resulting list of words is then printed to the console.


