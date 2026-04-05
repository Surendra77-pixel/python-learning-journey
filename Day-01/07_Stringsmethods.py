#strings methods in python and modify strings 

#strings are unmutable in python, which means that once a string is created, it cannot be changed. However, you can create a new string by modifying the original string using various string methods. Here are some common string methods in python:

a="The ai is the future"
b=a[:10] + "amazing " + a[10:] # The slicing a[:10] extracts the first 10 characters, and a[10:] extracts the remaining characters. By concatenating these with the new string "amazing ", we create a modified version of the original string.
print(b) # Output: The ai is amazing the future - The modified string b is "The ai is amazing the future", which is created by inserting "amazing " into the original string a at the appropriate position.

#1.upper()- the upper method converts all characters in a string to uppercase. Here is an example:
a="Surendra"
print(a.upper()) # Output: SURENDRA - The upper() method converts all characters in the string a to uppercase, resulting in "SURENDRA".

#2.lower()- the lower method converts all characters in a string to lowercase. Here is an example:  
a="Surendra"
print(a.lower()) # Output: surendra - The lower() method converts all characters in the string a to lowercase, resulting in "surendra".

#3.strip()- the strip method removes any leading and trailing whitespace from a string. Here is an example:
a="  surendra  "
print(a.strip()) # Output: surendra - The strip() method removes the leading and trailing whitespace from the string a, resulting in "surendra".

#4.lstrip()- the lstrip method removes any leading whitespace from a string. Here is an example:  
a="  surendra  "
print(a.lstrip()) # Output: surendra   - The lstrip() method removes the leading whitespace from the string a, resulting in "surendra   " (the trailing whitespace remains).

#5.rstrip()- the rstrip method removes any trailing whitespace from a string. Here is an example:  
a="  surendra  "
print(a.rstrip()) # Output:   surendra - The rstrip() method removes the trailing whitespace from the string a, resulting in "   surendra" (the leading whitespace remains).

#6.replace()- the replace method replaces all occurrences of a specified substring with another substring. Here is an example:
a="The ai is the future ai"
print(a.replace("ai","artificial intelligence")) # Output: The artificial intelligence is the future artificial intelligence - The replace() method replaces all occurrences of the substring "ai" with "artificial intelligence" in the string a, resulting in "The artificial intelligence is the future artificial intelligence". Note that both instances of "ai" are replaced in the resulting string.thus the replace

#6.1other example of replace method:
a="pizza"
print(a.replace("z","s")) # Output: pissa - The replace() method replaces all occurrences of the substring "z" with "s" in the string a, resulting in "pissa".
#explanation: In this code, we have a string a with the value "pizza". We use the replace() method to replace all occurrences of the substring "z" with "s". Since there are two "z" characters in "pizza", both of them are replaced, resulting in the new string "pissa".




#7.split()- the split method splits a string into a list of substrings based on a specified delimiter. Here is an example:
a="The ai is the future"
print(a.split()) # Output: ['The', 'ai', 'is', 'the', 'future'] - The split() method splits the string a into a list of substrings based on whitespace (the default delimiter), resulting in ['The', 'ai', 'is', 'the', 'future'].

#8.capitalize()- the capitalize method capitalizes the first character of a string and converts the rest of the characters to lowercase. Here is an example:
a="the ai is the future"
print(a.capitalize()) # Output: The ai is the future - The capitalize() method capitalizes the first character of the string a and converts the rest of the characters to lowercase, resulting in "The ai is the future".

#9.casefold()- the casefold method is similar to the lower method, but it is more aggressive in converting characters to lowercase. It is used for caseless matching of strings. Here is an example:
a="The ai is the future"
print(a.casefold()) # Output: the ai is the future - The casefold() method converts all characters in the string a to lowercase in a more aggressive way than lower(), resulting in "the ai is the future".

#10.center: returns a centered string here is the example:
a="Surendra"
print(a.center(14, "=")) # Output: ===Surendra=== - The center() method centers the string a within a field of width 14, using "=" as the fill character. The resulting string is "===Surendra===", which is centered with "=" characters on both sides.

#11.count - returns the number of occurrences of a substring in a string. Here is an example:
a="The Then That There"
print(a.count("Th")) # Output: 4 - The count() method counts the number of occurrences of the substring "Th" in the string a, resulting in 4 (it counts "Th" in "The", "Then", "That", and "There").

#12.encode- returns an encoded version of the string. Here is an example:
a="The ai is the future"
print(a.encode()) # Output: b'The ai is the future' - The encode() method encodes the string a using the default encoding (UTF-8) and returns a bytes object. The resulting output is b'The ai is the future', where the "b" prefix indicates that it is a bytes object.

#13.endswith- returns True if the string ends with a specified suffix, otherwise returns False. Here is an example:
a="The ai is the future"
print(a.endswith("future")) # Output: True - The endswith() method checks if the string a ends with the substring "future". Since it does, the method returns True.

#14.expandtabs- returns a copy of the string where all tab characters are replaced with spaces. Here is an example:
a="The\tai\tis\tthe\tfuture"
print(a.expandtabs(4)) # Output: The ai  is  the future - The expandtabs() method replaces each tab character ("\t") in the string a with a specified number of spaces (in this case, 4). The resulting string is "The    ai    is    the    future", where each tab has been replaced with 4 spaces.

#15.find,Index- returns the lowest index of the substring if it is found in the string, otherwise returns -1. Here is an example:
a="The ai is the future"
print(a.find("ai")) # Output: 4 - The find() method searches for the substring "ai" in the string a and returns the lowest index where it is found. In this case, "ai" is found at index 4, so the method returns 4. If the substring were not found, it would return -1.

#16.format- formats specified values in a string. Here is an example:
name="Surendra"
print("Hello, {}!".format(name)) # Output: Hello, Surendra! - The format() method is used to insert the value of the variable name into the string "Hello, {}!". The curly braces {} act as a placeholder for the value. When the format() method is called with the argument name, it replaces the placeholder with the value of name, resulting in "Hello, Surendra!". we learn in the next one

#17.isalnum- returns True if all characters in the string are alphanumeric (letters and numbers), otherwise returns False. Here is an example:
a="Surendra123"
print(a.isalnum()) # Output: True - The isalnum() method checks if all characters in the string a are alphanumeric. Since "Surendra123" consists of letters and numbers only, the method returns True. If there were any spaces or special characters, it would return False.

#18.isalpha- returns True if all characters in the string are alphabetic (letters only), otherwise returns False. Here is an example:
a="Surendra"
print(a.isalpha()) # Output: True - The isalpha() method checks if all characters in the string a are alphabetic. Since "Surendra" consists of letters only, the method returns True. If there were any spaces, numbers, or special characters, it would return False.

#19.title- returns a title-cased version of the string, where the first character of each word is capitalized and the rest are lowercase. Here is an example:
a="the ai is the future"
print(a.title()) # Output: The Ai Is The Future - The title() method converts the string a to title case, where the first character of each word is capitalized and the rest are lowercase. The resulting string is "The Ai Is The Future".

#20.startswith() and endswith() methods are used to check if a string starts or ends with a specified substring, respectively. Here is an example:
a="The ai is the future"
print(a.startswith("The")) # Output: True - The startswith() method checks if the string a starts with the substring "The". Since it does, the method returns True. 
a="The ai is the future"
print(a.endswith("future")) # Output: True - The endswith() method checks if the string a ends with the substring "future". Since it does, the method returns True.

#21.join()-used to join a list of strings into a single string with a specified separator. Here is an example:
my_list=["The","ai","is","the","future"]
print(" ".join(my_list)) # Output: The ai is the future - The join() method takes the list of strings my_list and joins them into a single string using a space (" ") as the separator. The resulting string is "The ai is the future". If we used a different separator, such as a hyphen ("-"), the output would be "The-ai-is-the-future".

#22.isupper-check wheather each character in the string is uppercase or not. Here is an example:
a="SURNDRA" 
print(a.isupper()) # Output: True - The isupper() method checks if all characters in the string a are uppercase. Since "SURNDRA" consists of uppercase letters only, the method returns True. If there were any lowercase letters, it would return False.

#23.islower-check whether each character in the string is lowercase or not. Here is an example:    
a="surendra"
print(a.islower()) # Output: True - The islower() method checks if all characters in the string a are lowercase. Since "surendra" consists of lowercase letters only, the method returns True. If there were any uppercase letters, it would return False.  

#24.extend()-the extend() method is not a string method, it is a list method. It is used to extend a list by appending all the items from another iterable (such as another list). Here is an example:
my_list=["The","ai","is","the","future"]
my_list.extend(["and","it","is","amazing"])
print(my_list) # Output: ['The', 'ai', 'is', 'the', 'future', 'and', 'it', 'is', 'amazing'] - The extend() method takes the list my_list and extends it by appending all the items from the list ["and", "it", "is", "amazing"]. The resulting list is ['The', 'ai', 'is', 'the', 'future', 'and', 'it', 'is', 'amazing']. Note that the extend() method modifies the original list in place and does not return a new list.

#concatenation- we can concatenate strings using the + operator. Here is an example:
a="The ai is the future"
b=" and it is amazing"
c=a+b
print(c) # Output: The ai is the future and it is amazing - The + operator is used to concatenate the strings a and b, resulting in the new string c, which is "The ai is the future and it is amazing".   

#precedence of operators- when concatenating strings with other operators, the precedence of operators is important. The + operator has a higher precedence than the * operator, so it will be evaluated first. Here is an example:
a="The ai is the future"
b=" and it is amazing"
c=a+b
print(c) # Output: The ai is the future and it is amazing - The + operator is used to concatenate the strings a and b, resulting in the new string c, which is "The ai is the future and it is amazing".    If we were to use the * operator to repeat a string, it would be evaluated after the + operator. For example:
a="The ai is the future"   
b=" and it is amazing"
c=a+b*2
print(c) # Output: The ai is the future and it is amazing and it is amazing - In this case, the + operator concatenates a and b first, resulting in "The ai is the future and it is amazing". Then, the * operator repeats the string b twice, resulting in " and it is amazing and it is amazing". Finally, the two results are concatenated together to produce the final output  "The ai is the future and it is amazing and it is amazing".     


age =25
is_student = True
if (age < 18) and is_student:
    print("You are a student and under 18.")
    #In this code, we have an if statement that checks if the age is less than 18 and if the is_student variable is True. If both conditions are met, it will print "You are a student and under 18." In this case, since age is 25, the condition age < 18 is False, so the code inside the if block will not be executed. If we change the age to 17, then the condition age < 18 would be True, and if is_student is also True, it would print the message.

    #the (age<18)- this brackets is called parentheses and it is used to group the condition age < 18 together. This is important because it ensures that the condition is evaluated correctly in conjunction with the logical operator and. The parentheses indicate that we want to evaluate age < 18 first before combining it with the is_student condition using the and operator. Without the parentheses, the expression would be evaluated differently, and it could lead to incorrect results..