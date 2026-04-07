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


 #---------------------------

 #There are some of the string formatting methods in python, such as f-strings, format() method, and old string formatting using % operator. Each of these methods allows us to create formatted strings by embedding variables and expressions within the string literals, making it easier to generate dynamic and readable output.

 #1.:<- left-align the text within the specified width-
text = "Hello"
print(f"{text:<10}") # Output: 'Hello     ' - The format specifier :<10 left-aligns the text "Hello" within a field of width 10, resulting in the output "Hello     " with extra spaces added to the right to fill the width.

#2.:> - right-align the text within the specified width-
text = "Hello"
print(f"{text:>10}") # Output: '     Hello' - The format specifier :>10 right-aligns the text "Hello" within a field of width 10, resulting in the output "     Hello" with extra spaces added to the left to fill the width.


#3.:^ - center-align the text within the specified width-
text = "Hello"
print(f"{text:^10}") # Output: '  Hello   ' - The format specifier :^10 center-aligns the text "Hello" within a field of width 10, resulting in the output "  Hello   " with extra spaces added to both sides to center the text within the width.


#4.:= - forces the padding to be placed after the sign (if any) and before the digits-
number = -42
print(f"{number:=10}") # Output: '-       42' - The format specifier :=10 forces the padding to be placed after the sign (if any) and before the digits, resulting in the output '-       42' with extra spaces added to the left to fill the width while keeping the negative sign immediately before the number.


#5.:+ - forces the sign to be used for both positive and negative numbers-
number = 42
print(f"{number:+10}") # Output: '      +42' - The format specifier :+10 forces the sign to be used for both positive and negative numbers, resulting in the output '      +42' with a plus sign added before the number and extra spaces added to the left to fill the width.


#6.:- - forces the sign to be used only for negative numbers-
number = 42
print(f"{number:-10}") # Output: '        42' - The format specifier :-10 forces the sign to be used only for negative numbers, resulting in the output '        42' with no sign for the positive number and extra spaces added to the left to fill the width.


#7,: - uses the default alignment and padding-
text = "Hello"
print(f"{text:10}") # Output: 'Hello     ' - The format specifier :10 uses the default alignment and padding, which is left-aligned for strings, resulting in the output "Hello     " with extra spaces added to the right to fill the width.


#8.:, - adds a comma as a thousand separator for numbers-
number = 1000000
print(f"{number:,}") # Output: '1,000,000' - The format specifier :, adds a comma as a thousand separator for the number 1000000, resulting in the output '1,000,000' which is easier to read for large numbers.


#9.:_ - adds an underscore as a thousand separator for numbers-
number = 1000000
print(f"{number:_}") # Output: '1_000_000' - The format specifier :_ adds an underscore as a thousand separator for the number 1000000, resulting in the output '1_000_000' which is another way to improve readability for large numbers.


#10.:b - formats the number as binary-
number = 42 
print(f"{number:b}") # Output: '101010' - The format specifier :b formats the number 42 as binary, resulting in the output '101010' which is the binary representation of the decimal number 42.


#11.:c- formats the number as a Unicode character-
number = 65
print(f"{number:c}") # Output: 'A' - The format specifier :c formats the number 65 as a Unicode character, resulting in the output 'A' which is the character corresponding to the Unicode code point 65 (the letter 'A').


#12.:d - formats the number as a decimal integer-
number = 42
print(f"{number:d}") # Output: '42' - The format specifier :d formats the number 42 as a decimal integer, resulting in the output '42' which is the standard decimal representation of the number.


#13.:e - formats the number in scientific notation-
number = 0.00042
print(f"{number:e}") # Output: '4.200000e-05' - The format specifier :e formats the number 0.00042 in scientific notation, resulting in the output '4.200000e-05' which represents the number in the form of a mantissa and an exponent.


#14.:f - formats the number as a fixed-point number-
number = 3.14159
print(f"{number:f}") # Output: '3.141590' - The format specifier :f formats the number 3.14159 as a fixed-point number, resulting in the output '3.141590' which is the standard decimal representation of the number with six decimal places by default.


#15.:g - formats the number in either fixed-point format or scientific notation, depending on the value and precision-
number = 0.00042
print(f"{number:g}") # Output: '0.00042' - The format specifier :g formats the number 0.00042 in either fixed-point format or scientific notation, depending on the value and precision. In this case, since the number is small and does not require scientific notation, it is formatted as '0.00042' in fixed-point format.


#16.:G - formats the number in either fixed-point format or scientific notation, depending on the value and precision, but uses uppercase letters for the exponent in scientific notation-
number = 0.00042    
print(f"{number:G}") # Output: '0.00042' - The format specifier :G formats the number 0.00042 in either fixed-point format or scientific notation, depending on the value and precision, but uses uppercase letters for the exponent in scientific notation. In this case, since the number is small and does not require scientific notation, it is formatted as '0.00042' in fixed-point format without any change from the :g specifier.


#17.:o - formats the number as octal-
number = 42
print(f"{number:o}") # Output: '52' - The format specifier :o formats the number 42 as octal, resulting in the output '52' which is the octal representation of the decimal number 42.


#18.:x - formats the number as hexadecimal with lowercase letters-
number = 42
print(f"{number:x}") # Output: '2a' - The format specifier :x formats the number 42 as hexadecimal with lowercase letters, resulting in the output '2a' which is the hexadecimal representation of the decimal number 42 using lowercase letters for values 10-15.


#19.:X - formats the number as hexadecimal with uppercase letters-
number = 42
print(f"{number:X}") # Output: '2A' - The format specifier :X formats the number 42 as hexadecimal with uppercase letters, resulting in the output '2A' which is the hexadecimal representation of the decimal number 42 using uppercase letters for values 10-15.


#20.:n - formats the number according to the current locale settings-
import locale
locale.setlocale(locale.LC_ALL, '')  # Set to the user's default locale
number = 1000000
print(f"{number:n}") # Output: '1,000,000' (or similar based on locale) - The format specifier :n formats the number 1000000 according to the current locale settings, which typically includes adding a comma as a thousand separator. The actual output may vary based on the user's locale settings, but it generally improves readability for large numbers.


#21.:% - formats the number as a percentage:
number = 0.75
print(f"{number:%}") # Output: '75.000000%' - The format specifier :% formats the number 0.75 as a percentage, resulting in the output '75.000000%' which represents the number as a percentage with six decimal places by default.

