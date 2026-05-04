
# Generators are functions that give you values one by one, only when you ask for them.

#The generators is a special type of function that returns an iterator. It allows you to iterate over a sequence of values without having to create and store the entire sequence in memory at once. This can be particularly useful when working with large datasets or infinite sequences.in simple word we can it returns values one at a time, instead of returning them all at once like a list or a tuple. This can save memory and improve performance when working with large datasets or infinite sequences.

#when the generator function is called, it does not execute the function body immediately. Instead, it returns a generator object that can be used to iterate over the values produced by the generator. The generator function uses the yield keyword to produce values one at a time. Each time the yield statement is encountered, the current state of the generator is saved, and the value is returned to the caller. The next time the generator is called, it resumes execution from where it left off, allowing you to retrieve the next value in the sequence.

#The generator allow you to iterate over data without storing the entire dataset in memory at once. This can be particularly useful when working with large datasets or infinite sequences, as it can help to reduce memory usage and improve performance. Additionally, generators can be used to create more efficient and readable code, as they allow you to write code that produces values on-the-fly, rather than having to create and manipulate large data structures in memory.

#normal function vs generator function-

#normal function
def normal_function():
    return [1, 2, 3]
#output: [1, 2, 3] - In this example, the normal_function is a regular function that returns a list of numbers from 1 to 3. When you call normal_function(), it creates the entire list in memory and returns it all at once. The output of this code will be [1, 2, 3], which is the complete list of numbers.

#generator function
def generator_function():
    yield 1
    yield 2
    yield 3
#output: <generator object generator_function at 0x7f8b8c8c8c8> - In this example, the generator_function is a generator function that uses the yield keyword to produce values one at a time. When you call generator_function(), it returns a generator object instead of a list. The output of this code will be something like <generator object generator_function at 0x7f8b8c8c8c8>, which indicates that it is a generator object. To get the values from the generator, you can use a loop or the next() function to retrieve each value one at a time.


#The generator saves memory

#generators are more memory efficient than normal functions because they produce values one at a time, rather than creating and storing the entire sequence in memory at once. This can be particularly beneficial when working with large datasets or infinite sequences, as it allows you to process data without consuming excessive memory resources. By using generators, you can iterate over data without having to load everything into memory, which can lead to improved performance and reduced memory usage.

def large_sequence(n):
    for i in range(n):
        yield i
gen = large_sequence(1000000)
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
#In this example, the large_sequence function is a generator that produces a sequence of numbers from 0 to n-1. When you call large_sequence(1000000), it returns a generator object that can be used to iterate over the sequence of numbers. The next() function is used to retrieve each value from the generator one at a time. This allows you to process the sequence without having to create and store the entire list of numbers in memory, which can save memory and improve performance when working with large datasets.and when it reaches the end of the sequence, it will raise a StopIteration exception, indicating that there are no more values to retrieve from the generator.

def simple_gen():
    yield 'Hello'
    yield 'World'
    yield 'Python'
for word in simple_gen():
print(word)
#output:
# Hello 
# World
# Python - In this example, the simple_gen function is a generator that produces a sequence of strings. When you call simple_gen(), it returns a generator object that can be used to iterate over the sequence of strings. The for loop is used to retrieve each value from the generator one at a time and print it. This allows you to process the sequence of strings without having to create and store the entire list of strings in memory, which can save memory and improve performance when working with large datasets.


#or 

def simple_gen():
    yield 'Hello'
    yield 'World'
    yield 'Python'
gen = simple_gen()
print(next(gen))  # Output: Hello
print(next(gen))  # Output: World
print(next(gen))  # Output: Python
#In this example, the simple_gen function is a generator that produces a sequence of strings. When you call simple_gen(), it returns a generator object that can be used to retrieve each value from the generator one at a time using the next() function. Each call to next(gen) retrieves the next value from the generator and prints it. This allows you to process the sequence of strings without having to create and store the entire list of strings in memory, which can save memory and improve performance when working with large datasets.

#when the generator reaches the end of the sequence, it will raise a StopIteration exception, indicating that there are no more values to retrieve from the generator. You can handle this exception using a try-except block to gracefully exit the loop when the generator is exhausted.
def simple_gen():
    yield 1
    yield 2
gen= simple_gen()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # This will raise StopIteration exception
#In this example, the simple_gen function is a generator that produces a sequence of numbers. When you call simple_gen(), it returns a generator object that can be used to retrieve each value from the generator one at a time using the next() function. The first two calls to next(gen) retrieve the values 1 and 2, respectively. However, when you call next(gen) a third time, it will raise a StopIteration exception because there are no more values to retrieve from the generator. You can handle this exception using a try-except block to gracefully exit the loop when the generator is exhausted.

#Generators vs list comprehensions

#Generators and list comprehensions are both powerful tools in Python for creating sequences of values, but they have some key differences.

#1. Memory Usage: Generators are more memory efficient than list comprehensions because they produce values one at a time, rather than creating and storing the entire sequence in memory at once. This can be particularly beneficial when working with large datasets or infinite sequences.
#2. Syntax: List comprehensions use a concise syntax that allows you to create lists in a single line of code, while generators use the yield keyword to produce values one at a time. This can make list comprehensions more readable and easier to understand for simple cases, while generators may require more lines of code and may be less intuitive for beginners.
#3. Use Cases: List comprehensions are typically used when you want to create a new list based on an existing iterable, while generators are more suitable for situations where you want to produce values on-the-fly, such as when processing large datasets or working with infinite sequences.
#In summary, generators are more memory efficient than list comprehensions because they produce values one at a time, rather than creating and storing the entire sequence in memory at once. This can be particularly beneficial when working with large datasets or infinite sequences, as it allows you to process data without consuming excessive memory resources. By using generators, you can iterate over data without having to load everything into memory, which can lead to improved performance and reduced memory usage.

#List comprehension - create a list 

list_comp=[x*X for x in range(5)]
print(list_comp)  # Output: [0, 1, 4, 9, 16] - In this example, the list comprehension creates a new list by iterating over the range of numbers from 0 to 4 and multiplying each number by itself (x*X). The resulting list contains the squares of the numbers in the range.

#Generator expression - create a generator
gen_exp=(x*X for x in range(5))
print(gen_exp)  # Output: <generator object <genexpr> at 0x7f8b8c8c8c8>-[0, 1, 4, 9, 16] - In this example, the generator expression creates a generator object that produces the squares of the numbers in the range from 0 to 4. When you print gen_exp, it shows that it is a generator object. To retrieve the values from the generator, you can use a loop or the next() function to get each value one at a time.


#generator with the sum expression

gen_exp=(x*X for x in range(5))
print(sum(gen_exp))  # Output: 30 - In this example, the generator expression creates a generator object that produces the squares of the numbers in the range from 0 to 4. When you pass gen_exp to the sum() function, it iterates over the generator and sums up the values produced by the generator. The output will be 30, which is the sum of the squares of the numbers from 0 to 4 (0 + 1 + 4 + 9 + 16 = 30). This demonstrates how you can use a generator expression with a built-in function like sum() to efficiently process data without having to create and store an intermediate list in memory.


#Fibonacci sequence using a generator

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
fib_gen = fibonacci(10)
for num in fib_gen:
    print(num)
#Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34 - In this example, the fibonacci function is a generator that produces the Fibonacci sequence up to the nth number. The generator uses the yield keyword to produce each value in the sequence one at a time. When you call fibonacci(10), it returns a generator object that can be used to iterate over the Fibonacci sequence. The for loop is used to retrieve each value from the generator and print it, resulting in the first 10 numbers in the Fibonacci sequence being printed. This demonstrates how you can use a generator to efficiently generate and process a sequence of values without having to create and store the entire sequence in memory at once.

#Generators methods(send(), throw(), close())

#1. send():

#  The send() method is used to send a value to a generator. It allows you to resume the generator's execution and pass a value that can be used within the generator function. When you call send(value), the generator will resume execution from where it last yielded and will receive the value sent as an argument. This can be useful for controlling the flow of the generator and providing input to it while it is running.

def echo_generator():
    while True:
        value = yield
        print(f"Received: {value}")
gen = echno_generator()
next(gen)  # Start the generator
gen.send("Hello")  # Output: Received: Hello
gen.send("World")  # Output: Received: World - In this example, the echno_generator function is a generator that uses the yield keyword to receive values sent to it. When you call next(gen), it starts the generator and waits for a value to be sent. The gen.send("Hello") call sends the string "Hello" to the generator, which resumes execution and prints "Received: Hello". Similarly, gen.send("World") sends the string "World" to the generator, which resumes execution again and prints "Received: World". This demonstrates how you can use the send() method to interact with a generator and provide input while it is running.

#next() is used to retrieve the next value from a generator. It resumes the generator's execution and returns the next value produced by the generator. If the generator has no more values to produce, it raises a StopIteration exception.
#example:

# Generator function
def echo_generator():
    while True:
        value = yield   # Wait to receive a value
        print(f"Received: {value}")


# Create generator object
gen = echo_generator()

# Step 1: Start the generator (very important)
next(gen)   # or gen.send(None)

# Step 2: Send values to generator
gen.send("Hello")   # Output: Received: Hello
gen.send("World")   # Output: Received: World
gen.send("Python")  # Output: Received: Python


#2.close(): 

# The close() method is used to stop a generator. When you call close() on a generator, it raises a GeneratorExit exception inside the generator function, which can be caught and handled if needed. This allows you to gracefully exit the generator and perform any necessary cleanup before it is terminated.

def my_gen():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Generator is closing...")    
    gen=my_gen()
    print(next(gen))  # Output: 1
    print(next(gen))  # Output: 2
    gen.close()  # Output: Generator is closing... - In this example, the echo_generator function is a generator that produces a sequence of numbers. The finally block is used to print a message when the generator is closed. When you call gen.close(), it raises a GeneratorExit exception inside the generator function, which triggers the finally block and prints "Generator is closing...". This demonstrates how you can use the close() method to gracefully exit a generator and perform any necessary cleanup before it is terminated.

    #3.throw():
    
    #  The throw() method is used to raise an exception inside a generator. When you call throw(exception), it raises the specified exception at the point where the generator is currently paused (i.e., where it last yielded). This can be useful for handling errors or controlling the flow of the generator based on certain conditions.

def my_gen():
    try:
        yield 1
        yield 2
        yield 3
    except ValueError as e:
        print(f"Caught exception: {e}") 
gen = my_gen()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
gen.throw(ValueError("An error occurred"))  # Output: Caught exception: An error occurred - In this example, the my_gen function is a generator that produces a sequence of numbers. The except block is used to catch a ValueError exception that may be thrown inside the generator. When you call gen.throw(ValueError("An error occurred")), it raises a ValueError exception at the point where the generator is currently paused (after yielding 2). The except block catches the exception and prints "Caught exception: An error occurred". This demonstrates how you can use the throw() method to raise an exception inside a generator and handle it appropriately.
