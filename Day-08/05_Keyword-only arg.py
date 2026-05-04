
#The keyword-only parameters are defined in the function signature using an asterisk (*) to indicate that the parameters after the asterisk are keyword-only. This means that when calling the function, you must specify the parameter names for these parameters, and you cannot provide them as positional arguments.

#----- to use the kryword-only aruguments * -add this before the aruguments in the function definition.

def my_function(*, name, age):
    print(f"my name is {name} and my age is {age}")
my_function(name="surendra", age="20")#output: my name is surendra and my age is 20 - In this example, the function  my_function is defined with keyword-only parameters (name and age) using an asterisk (*). When we call the function, we must specify the parameter names (name and age) along with their corresponding values ("surendra" and "20") in the function call. The function then executes its code and prints "my name is surendra and my age is 20". This demonstrates that when keyword-only parameters are used, we must use keyword arguments to specify them when calling the function.


#2. without * ,  you are allowed to use positional arguments evin if the function excepts keyword arguments 

def my_function(name, age):
    print(f"my name is {name} and my age is {age}")
my_function("surendra", "20")#output: my name is surendra and my age is 20 - In this example, the function my_function is defined without using keyword-only parameters. This allows us to use positional arguments when calling the function. We provide the arguments "surendra" and "20" in the correct order, and the function executes its code, resulting in printing "my name is surendra and my age is 20". This demonstrates that when keyword-only parameters are not used, we can use positional arguments to specify the parameters when calling the function.  


#3.with *, if you try to provide the arguments as positional arguments when calling the function, it will raise a TypeError. For example:
def my_function(*, name, age):
    print(f"my name is {name} and my age is {age}")
my_function("surendra", "20")#output: TypeError: my_function() takes 0 positional arguments but 2 were given - In this example, the function my_function is defined with keyword-only parameters (name and age) using an asterisk (*). When we try to call the function with positional arguments ("surendra" and "20"), it raises a TypeError because the function expects these parameters to be provided as keyword arguments, not as positional arguments. To fix this error, we need to call the function with keyword arguments like this: my_function(name="surendra", age="20").

#6.combing the positional-only and keyword-only parameters:

def my_function(positional_arg, *, keyword_arg):
    print(f"Positional argument: {positional_arg}")
    print(f"Keyword argument: {keyword_arg}")
my_function("positional value", keyword_arg="keyword value")#output: Positional argument: positional value Keyword argument: keyword value - In this example, the function my_function is defined with one positional-only parameter (positional_arg) and one keyword-only parameter (keyword_arg). When we call the function, we provide a positional argument ("positional value") for the positional-only parameter and a keyword argument (keyword_arg="keyword value") for the keyword-only parameter. The function then executes its code and prints the values of both parameters. This demonstrates how we can combine positional-only and keyword-only parameters in a single function definition in Python.

#7. unpacking the keyword-only parameters-

def greet(name, location):
    print("Hi there", name, "how is the weather in", location)
greet(name="Alice", location="New York")
# Output: Hi there Alice how is the weather in New York
my_dict = {"name": "Alice", "location": "New York"}
greet(**my_dict)
# The ** operator unpacks the dictionary, passing its key-value pairs as keyword arguments to the function.
# Output: Hi there Alice how is the weather in New York

