#There are few type of the conversions in python:

#Type conversion
#Type casting
#Type checking
 
                                   #Type conversion-

#  The automatic conversion of one data type to another is called type conversion. It is also known as implicit type conversion or coercion. In this process, Python automatically converts one data type to another when it is necessary to perform an operation. For example:

x=5 # integer
y=2.0 #float
z=x+y # The integer 5 is automatically converted to a float 5.0 before the addition operation is performed.
print(z) # Output: 7.0


                                    #Type casting-

#  Type casting is the process of converting a variable from one data type to another explicitly. In Python, you can use built-in functions like int(), float(), str(), etc., to perform type casting. For example:


x=5 # integer
y=float(x) # The integer 5 is explicitly converted to a float 5.0 using the float() function.
print(y) # Output: 5.0

                                         #typechecking-
                                         
# The types checking is the process of verifying the data type of a variable or an expression. In Python, you can use the built-in type() function to check the data type of a variable. For example:

x=["Apple","Banana","Cherry"] # list   
print(type(x)) # Output: <class 'list'>.