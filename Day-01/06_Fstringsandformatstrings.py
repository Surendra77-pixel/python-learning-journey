                                #fstrings-
                                 
# we can combine the strings and variables using f-strings in python. F-strings are a way to format strings in python by embedding expressions inside string literals. They are denoted by prefixing the string with the letter 'f' or 'F'. Here is an example of how to use f-strings:    
name="Surendra"
age=25
print(f"My name is {name} and I am {age} years old.") # Output: My name is Surendra and I am 25 years old. - The f-string allows us to embed the variables name and age directly within the string, making it easier to read and write formatted strings.   

#2f- The 2f is a format specifier that is used to format floating-point numbers to a specific number of decimal places. In this case, 2f means that the number will be formatted to 2 decimal places. Here is an example:
a=3.14159
print(f"The value of pi is approximately {a:.2f}.") # Output: The value of pi is approximately 3.14. - The format specifier :.2f formats the value of a to 2 decimal places, resulting in the output "3.14".    

price=59
text=f"The price of the item is ${price:.2f}." # The format specifier :.2f formats the value of price to 2 decimal places, resulting in the output "59.00".
print(text) # Output: The price of the item is $59.00. - The f-string allows us to embed the variable price directly within the string, and the format specifier :.2f ensures that it is displayed with 2 decimal places, giving us a more polished output. 

#we can do the same thing with the format() method in python. The format() method is another way to format strings in python by using placeholders and passing values as arguments. Here is an example of how to use the format() method:
name="Surendra"
age=25
print("My name is {} and I am {} years old.".format(name, age)) # Output: My name is Surendra and I am 25 years old. - The format() method allows us to use placeholders {} in the string and pass the variables name and age as arguments to fill those placeholders, resulting in a formatted string.     

#we can do some operations in the f-string as well. Here is an example:
x=10
y=20
print(f"The sum of {x} and {y} is {x+y}.") # Output: The sum of 10 and 20 is 30. - The f-string allows us to perform the addition operation directly within the string by embedding the expression {x+y}, which evaluates to 30, giving us a dynamic and formatted output.

#using some of the expressions in f-string
name="python"
print(f"The length of the name is {len(name)}.") # Output: The length of the name is 6. - The f-string allows us to use the len() function directly within the string by embedding the expression {len(name)}, which evaluates to 6, giving us a dynamic and formatted output that shows the length of the name variable.


name="python"
print(f"the popular language is now{name.upper()}.") # Output: The popular language is now PYTHON. - The f-string allows us to use the upper() method directly within the string by embedding the expression {name.upper()}, which converts the value of name to uppercase, resulting in "PYTHON" in the output.

#unpacking a collection in f-string- we can also unpack a collection of values directly within an f-string. Here is an example:
languages="python"
a,b,c,d,e,f=languages
print(a)
print(b)
print(c)
print(d)
print(e)
print(f) # Output: p
          # y
          # t
          # h
          # o
          # n

#old string formatting in Python is also called “printf-style formatting” (because it comes from the C language style).

#-%s-this is used for the string formating here is the example
name = "Surendra"
age = 21
print("My name is %s and I am %d years old" % (name, age)) #this gives the ouput Sas the My name is Surendra and I am 21 years old - This is not used now in the python 3.1
 
 #%d - used for the integerd
 #%f - used for the floating point numbers
 #%-used for the number of digits 


 #Thus the strings is used .