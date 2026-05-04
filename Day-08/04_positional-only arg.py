
#The positional-only parameters are defined in the function signature using a slash (/) to indicate that the parameters before the slash are positional-only. This means that when calling the function, you must provide arguments for these parameters in the correct order, and you cannot use keyword arguments to specify them.The keyword is not used in this type 

#----- to specify the positional-only aruguments ./ -add this after the aruguments in the function definition.

def my_function(name, age, /):
    print(f"my name is {name} and my age is {age}")
my_function("surendra","20")#output: my name is surendra and my age is 20 - In this example, the function my_function is defined with two positional-only parameters, name and age. When we call the function with the arguments "surendra" and "20", it executes its code and prints "my name is surendra and my age is 20". Since these parameters are positional-only, we cannot use keyword arguments to specify them when calling the function.

#2.without using the positional-only parameters:

#with out the positonal-only parameters , you are actually allowed to use keyword arguments to specify the parameters when calling the function. For example:

def my_function(name, age):
    print(f"my name is {name} and my age is {age}")
my_function(name="surendra", age="20")#output: my name is surendra and my age is 20 - In this example, the function my_function is defined without using positional-only parameters. This allows us to use keyword arguments when calling the function. We specify the parameter names (name and age) along with their corresponding values ("surendra" and "20") in the function call. The function then executes its code and prints "my name is surendra and my age is 20". This demonstrates that when positional-only parameters are not used, we can use keyword arguments to specify the parameters in any order when calling the function.


#if in case you defined the positional-only parameters and you try to use keyword arguments to specify them when calling the function, it will raise a TypeError. For example:

def my_function(name, age, /):
    print(f"my name is {name} and my age is {age}")
my_function(name="surendra", age="20")#output: TypeError: my_function() got some positional-only arguments passed as keyword arguments - In this example, the function my_function is defined with positional-only parameters (name and age). When we try to call the function using keyword arguments (name="surendra", age="20"), it raises a TypeError because the function expects these parameters to be provided as positional arguments, not as keyword arguments. To fix this error, we need to call the function with positional arguments like this: my_function("surendra", "20").


#unpacking the positional-only parameters-

# Define a function that takes two arguments: 'name' and 'location'
def greet(name, location):
    # Print a greeting message using the provided arguments
    print("Hi there", name, "how is the weather in", location)

# Call the function using keyword arguments
greet(name="Alice", location="New York")  
# Output: Hi there Alice how is the weather in New York

# Create a dictionary with keys matching the function's parameter names
my_dict = {"name": "Alice", "location": "New York"}

# Call the function using dictionary unpacking
greet(**my_dict)  
# The ** operator unpacks the dictionary, passing its key-value pairs 
# as keyword arguments to the function.
# Output: Hi there Alice how is the weather in New Yorkz


#how to unpack aruguments in the function definition-

def greet(*, name, location):
    print("Hi there", name, "how is the weather in", location)
greet(name="Alice", location="New York")
# Output: Hi there Alice how is the weather in New York
my_dict = {"name": "Alice", "location": "New York"}
greet(**my_dict)
# The ** operator unpacks the dictionary, passing its key-value pairs as keyword arguments to the function.
# Output: Hi there Alice how is the weather in New York
 

