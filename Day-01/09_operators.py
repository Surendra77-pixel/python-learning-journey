#operators-The operators are used to perform operations on variables and values. In Python, there are several types of operators, including:

#1. Arithmetic operators: These operators are used to perform mathematical operations such as addition, subtraction, multiplication, division, modulus, exponentiation, and floor division. Examples include +, -, *, /, %, **, and //.

#2. Comparison operators: These operators are used to compare two values and return a boolean result. Examples include ==, !=, >, <, >=, and <=.

#3. Logical operators: These operators are used to combine multiple boolean expressions and return a boolean result. Examples include and, or, and not.

#4. Assignment operators: These operators are used to assign values to variables. Examples include =, +=, -=, *=, /=, %=, **=, and //=.

#5. Bitwise operators: These operators are used to perform bitwise operations on integers. Examples include &, |, ^, ~, <<, and >>.

#6. Identity operators: These operators are used to compare the memory locations of two objects. Examples include is and is not.

#7. Membership operators: These operators are used to test if a value is present in a sequence (such as a list, tuple, or string). Examples include in and not in.

#arithmetic operators-
a=10
b=5
print(a+b) #Output: 15 - The + operator performs addition, resulting in the sum of a and b, which is 15.
print(a-b) #Output: 5 - The - operator performs subtraction, resulting in the difference between a and b, which is 5.
print(a*b) #Output: 50 - The * operator performs multiplication, resulting in the product of a and b, which is 50.
print(a/b) #Output: 2.0 - The / operator performs division, resulting   in the quotient of a and b, which is 2.0.
print(a%b) #Output: 0 - The % operator performs modulus, resulting in the remainder of the division of a by b, which is 0.
print(a**b) #Output: 100000 - The ** operator performs exponentiation, resulting in a raised to the power of b, which is 100000.
print(a//b) #Output: 2 - The // operator performs floor division, resulting in the quotient of a divided by b, rounded down to the nearest whole number, which is 2.    

#comparison operators-
x=10
y=20
print(x==y) #Output: False - The == operator checks if x is equal to y, which is false since 10 is not equal to 20.
print(x!=y) #Output: True - The != operator checks if x is not equal to y, which is true since 10 is not equal to 20.
print(x>y) #Output: False - The > operator checks if x is greater than y, which is false since 10 is not greater than 20.
print(x<y) #Output: True - The < operator checks if x is less than y, which is true since 10 is less than 20.
print(x>=y) #Output: False - The >= operator checks if x is greater than or equal to y, which is false since 10 is not greater than or equal to 20.
print(x<=y) #Output: True - The <= operator checks if x is less than or equal to y, which is true since 10 is less than or equal to 20. 

#logical operators-
a=True
b=False 
print(a and b) #Output: False - The and operator returns true if both a and b are true, which is false since b is false.
print(a or b) #Output: True - The or operator returns true if at least one of a or b is true, which is true since a is true.
print(not a) #Output: False - The not operator returns the opposite of a, which is false since a is true.   

#assignment operators-
x=10
print(x) #Output: 10 - The = operator assigns the value 10 to the variable x.
x+=5
print(x) #Output: 15 - The += operator adds 5 to x and assigns the result back to x.
x-=3
print(x) #Output: 12 - The -= operator subtracts 3 from x and assigns the result back to x.
x*=2
print(x) #Output: 24 - The *= operator multiplies x by 2 and assigns the result back to x.
x/=4
print(x) #Output: 6.0 - The /= operator divides x by 4 and assigns the result back to x.
x%=3
print(x) #Output: 0.0 - The %= operator calculates the remainder of x divided by 3 and assigns the result back to x.
x**=2
print(x) #Output: 0.0 - The **= operator raises x to the power of 2 and assigns the result back to x.
x//=2
print(x) #Output: 0.0 - The //= operator performs floor division of x by 2 and assigns the result back to x.    

#bitwise operators-
a=5 # In binary: 0101
b=3 # In binary: 0011
print(a & b) #Output: 1 - The & operator performs bitwise AND, resulting in 0001.
print(a | b) #Output: 7 - The | operator performs bitwise OR, resulting in 0111.
print(a ^ b) #Output: 6 - The ^ operator performs bitwise XOR, resulting in 0110.
print(~a)    #Output: -6 - The ~ operator performs bitwise NOT, resulting in 11111010.
print(a << 1) #Output: 10 - The << operator performs left shift, resulting in 1010.
print(a >> 1) #Output: 2 - The >> operator performs right shift, resulting in 0010.

#identity operators-
x=10        
y=10
print(x is y) #Output: True - The is operator checks if x and y refer to the same object in memory, which is true since small integers are cached by Python.
print(x is not y) #Output: False - The is not operator checks if x and y do not refer to the same object in memory, which is false since x and y refer to the same object.

#membership operators-
my_list = [1, 2, 3, 4, 5]   
print(3 in my_list) #Output: True - The in operator checks if 3 is present in my_list, which is true.
print(6 in my_list) #Output: False - The in operator checks if 6 is present in my_list, which is false.
print(3 not in my_list) #Output: False - The not in operator checks if 3 is not present in my_list, which is false since 3 is present.
print(6 not in my_list) #Output: True - The not in operator checks if 6 is not present in my_list, which is true since 6 is not present.    

#the numbership operators with the strings-
my_string = "Hello, World!"
print("Hello" in my_string) #Output: True - The in operator checks if the substring "Hello" is present in my_string, which is true.
print("Python" in my_string) #Output: False - The in operator checks if the substring "Python" is present in my_string, which is false.
print("Hello" not in my_string) #Output: False - The not in operator checks if the substring "Hello" is not present in my_string, which is false since "Hello" is present.
print("Python" not in my_string) #Output: True - The not in operator checks if the substring "Python" is not present in my_string, which is true since "Python" is not present.

#Thus the operators are used to perform various operations on variables and values in Python, allowing us to manipulate data and create complex expressions.


#precedence of operators- The precedence of operators determines the order in which operations are performed in an expression. In Python, the precedence of operators is as follows (from highest to lowest):
#1. Parentheses ()
                    #the parentheses operator has the highest precedence, which means that any expression inside parentheses will be evaluated first. For example, in the expression 2 * (3 + 4), the addition inside the parentheses will be evaluated first, resulting in 2 * 7, which gives us 14.

            #example of operator precedence with parentheses:

print((100 + 50) * 2) #Output: 300 - In this expression, the parentheses around (100 + 50) ensure that the addition is performed first, resulting in 150. Then, the multiplication by 2 is performed, giving us the final result of 300.

#2. Exponentiation **   
                    #the exponentiation operator has the next highest precedence, which means that it will be evaluated after parentheses but before other operators. For example, in the expression 2 ** 3 + 4, the exponentiation will be evaluated first, resulting in 8 + 4, which gives us 12.
            
            #example of operator precedence with exponentiation:
print(2 ** 3 + 4) #Output: 12 - In this expression, the exponentiation operator ** is evaluated first, resulting in 8. Then, the addition of 4 is performed, giving us the final result of 12.


#3. Associativity of operators- The associativity of operators determines the order in which operators of the same precedence are evaluated in an expression. In Python, most operators are left-associative, which means that they are evaluated from left to right. For example, in the expression 10 - 5 + 2, the subtraction will be evaluated first (10 - 5), resulting in 5, and then the addition will be evaluated (5 + 2), giving us 7.

#example of operator associativity:
print(10 - 5 + 2) #Output: 7 - In this expression, the subtraction operator - is evaluated first, resulting in 5. Then, the addition operator + is evaluated, giving us the final result of 7.
