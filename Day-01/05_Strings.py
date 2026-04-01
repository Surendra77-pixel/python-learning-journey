#strings in python

#The strings in the python plays a crucial role in programming as they are used to represent and manipulate text data. A string is a sequence of characters enclosed in either single quotes (' ') or double quotes (" "). Strings can contain letters, numbers, symbols, and whitespace characters. They are immutable, meaning that once a string is created, it cannot be changed. However, you can create new strings by concatenating or slicing existing strings.

#what happens when we use the double quotes in the string??

print(""" This is surendra
      im here to learn python""") # Output: This is surendra
                                        # im here to learn python - what happens when we use the double quotes in the string?? - it allows us to create a multi-line string, which can span multiple lines of text. This is useful for creating long strings or for including line breaks in the string without using escape characters.

#strings in array -The strings as array i also call these as the index which means the unicode character 

a="The python is the interesting language"
print(a[0]) # Output: T
print(a[1]) # Output: h

#looping through the string- by using the for loop the string can be looped through each character in the string one by one. Here is an example:

for x in "This is surendra":
    print(x) # Output: T
             # h
             # i
             # s
             #  
             # i
             # s
             #  
             # s
             # u
             # r
             # e
             # n
             # d
             # r
             # a

#while im going to the strings i got a doubt which is how to check the length of the string??- we can use the built-in len() function to check the length of a string. Here is an example:

a="The python is the interesting language"
print(len(a)) # Output: 39 - The len() function returns the number of characters it includes spaces and punctuation in the string. In this case, the string "The python is the interesting language" has 39 characters, including spaces and punctuation.

#check string- we can use the in keyword to check if a substring exists within a string. they are in , not , if , if not  Here is an example:

#in
a="The python is the interesting language"
print("python" in a) # Output: True - The in keyword checks if the substring    

#not
a="The python is the interesting language"
print("java" not in a) # Output: True - The not in keyword checks if

#if
a="The python is the interesting language"
if "python" in a:
    print("Yes, 'python' is present in the string.")
# Output: Yes, 'python' is present in the string. - The if statement checks if the substring "python" is present in the string a. If it is, it prints a message confirming that it is present.

#if not
a="The python is the interesting language"  
if "java" not in a:
    print("No, 'java' is not present in the string.") 
    #output: No, 'java' is not present in the string. - The if statement checks if the substring "java" is not present in the string a. If it is not, it prints a message confirming that it is not present.

#slicing the string- we can use slicing to extract a portion of a string. The syntax for slicing is string[start:end], where start is the index of the first character to include and end is the index of the first character to exclude. Here is an example:

b="The python is the interesting language"
print(b[2:5])# Output: e p - The slicing b[2:5] extracts the characters from index 2 to index 4 (5 is excluded) from the string b, resulting in "e p".

#slice from start:

A="This is surendra "
print(A[:4]) # Output: This - The slicing A[:4] extracts the characters from the beginning of the string A up to index 3 (4 is excluded), resulting in "This".

#slice from end:

a="The himalayas is the highest mountain range in the world"
print(a[5:])# Output: himalayas is the highest mountain range in the world - The slicing a[5:] extracts the characters from index 5 to the end of the string a, resulting in "himalayas is the highest mountain range in the world".

#negative slice- we can also use negative indices to slice a string. Negative indices count from the end of the string, with -1 being the last character. Here is an example:

x="The ai is the future"
print(x[-6:-1]) # Output: futur - The slicing x[-6:-1] extracts the characters from index -6 to index -2 (the last character is excluded) from the string x, resulting in "futur".

#negative slice from end:

a="The ai is the future"
print(a[-6:]) # Output: future - The slicing a[-6:] extracts the characters from index -6 to the end of the string a, resulting in "future".

#negative slice from start:

a="The ai is the future"
print(a[:-6]) # Output: The ai is the - The slicing a[:-6] extracts the characters from the beginning of the string a up to index -7 (the last 6 characters are excluded), resulting in "The ai is the".

#reversing a string- we can reverse a string using slicing with a step of -1. Here is an example:

a="The ai is the future"
print(a[::-1]) # Output: erutuf eht si ia ehT - The slicing a[::-1] reverses the string a by starting from the end and moving backwards with a step of -1, resulting in "erutuf eht si ia ehT".

