
#                Math module in Python

#1. The math module in Python is a built-in module that provides mathematical functions and constants. It includes functions for performing mathematical operations such as trigonometric functions, logarithmic functions, and power functions, as well as constants such as pi and e.

#2. To use the math module, you need to import it at the beginning of your Python script. This allows you to access the functions and constants defined in the math module.

import math

#3. Some common functions provided by the math module include:

#1.pi():

#The math.pi constant represents the value of pi (approximately 3.14159). For example, math.pi will return the value of pi.

import math
print(math.pi) #Output- 3.141592653589793

#2.sqrt():

#The math.sqrt() function calculates the square root of a number. For example, math.sqrt(16) will return 4.0.

import math
result = math.sqrt(16)
print(result) #Output- 4.0

#3.sin():
#The math.sin() function calculates the sine of an angle (in radians). For example, math.sin(math.pi/2) will return 1.0.
import math
result = math.sin(math.pi/2)
print(result) #Output- 1.0

#4.cos():

#The math.cos() function calculates the cosine of an angle (in radians). For example, math.cos(0) will return 1.0.
import math
result = math.cos(0)
print(result) #Output- 1.0

#5.pow():

#The math.pow() function calculates the power of a number. For example, math.pow(2, 3) will return 8.0.
import math
result = math.pow(2, 3)
print(result) #Output- 8.0

#6.log():

#The math.log() function calculates the natural logarithm of a number. For example, math.log(math.e) will return 1.0.

import math
result = math.log(math.e)
print(result) #Output- 1.0


#7.floor():

#The math.floor() function returns the largest integer less than or equal to a given number. For example, math.floor(3.7) will return 3.

import math
result = math.floor(3.7)
print(result) #Output- 3


#8.ceil():
#The math.ceil() function returns the smallest integer greater than or equal to a given number. For example, math.ceil(3.2) will return 4.

import math
result = math.ceil(3.2)
print(result) #Output- 4

# to check what functions the module got , we can use the dir() function and the help() function to get the documentation of the module and its functions.

#If you need to use a specific function from the math module, you can import only that function using the from keyword. For example, from math import sqrt will allow you to use the sqrt() function directly without prefixing it with math.

from math import sqrt
result = sqrt(16)
print(result) #Output- 4.0

#It is possible to import multiple functions at once using the from keyword. For example, from math import sqrt, pi will allow you to use both the sqrt() function and the pi constant directly without prefixing them with math.

from math import sqrt, pi
result = sqrt(16)
print(result) #Output- 4.0
print(pi) #Output- 3.141592653589793

#If you want to import all functions and constants from the math module, you can use the wildcard import syntax. However, it is generally not recommended to use wildcard imports as it can lead to namespace pollution and make it harder to understand where certain functions or constants are coming from.

from math import *
result = sqrt(16)
print(result) #Output- 4.0
print(pi) #Output- 3.141592653589793

#When we import we can also rename the name of the function 

from math import sqrt as square_root
result = square_root(16)
print(result) #Output- 4.0 - In this example, we have imported the sqrt() function from the math module and renamed it to square_root using the as keyword. We can then use square_root() to calculate the square root of a number, which returns 4.0 in this case. This demonstrates how you can import a function from a module and give it a different name in your code using the as keyword.






