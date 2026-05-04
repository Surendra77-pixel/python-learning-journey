
#Recursion--

#A recursion is a common mathmatical and programming technique in which a function calls itself in order to solve a problem. It typically involves a base case that stops the recursion and a recursive case that breaks the problem into smaller subproblems.

#The developer should be careful with recursion as it can be quite easy to slip into writing a function Which never terminates all one, but excuse excess amount of memory or processor power. However, when we return correctly, recursion can be a very efficient and mathematically elegant approach to programming. 

#example of the recursion-

def count_down(n):
    if n <= 0:
        print("Done!")
    else:
        if n > 0:
            print(n)
            count_down(n-1)
count_down(5)#output: 5 4 3 2 1 Done! - In this example, the function count_down takes a positive integer n as an argument. It checks if n is less than or equal to 0, in which case it prints "Done!" and stops the recursion. If n is greater than 0, it prints the current value of n and then calls itself with n-1. This process continues until n reaches 0, at which point the base case is reached and the recursion stops. The output of this code will be the numbers from 5 down to 1 followed by "Done!".

#At here everyone gets the doubt that how the function count_down is able to call itself. The answer is that in Python, functions are first-class objects, which means they can be treated like any other object, such as integers or strings. When we define a function, it creates a function object that can be called by its name. In the case of count_down, when we call count_down(n-1), it is calling the same function object with a different argument (n-1). This allows the function to call itself recursively until it reaches the base case.

#Another doubt is the else is crt but why if also executed in the output. The answer is that in the code, the if statement checks if n is less than or equal to 0. If this condition is true, it prints "Done!" and stops the recursion. However, if n is greater than 0, the else block is executed, which prints the current value of n and then calls count_down(n-1). This means that for each positive value of n, both the if and else blocks are executed in sequence. The if block will only execute when n reaches 0 or a negative value, at which point it will print "Done!" and stop the recursion.


#2.In the recursion there are two main components: the base case and the recursive case. The base case is the condition under which the recursion will stop, while the recursive case is where the function calls itself with modified arguments to approach the base case. In the example of count_down, the base case is when n is less than or equal to 0, at which point it prints "Done!" and stops the recursion. The recursive case is when n is greater than 0, where it prints the current value of n and then calls itself with n-1, which brings it closer to the base case. This structure allows the function to break down the problem into smaller subproblems until it reaches a point where it can stop, ensuring that the recursion does not go on indefinitely.

#-Without the base case, the recursion would continue indefinitely, leading to a stack overflow error. The base case is essential to ensure that the recursion terminates properly and does not consume excessive resources. In the count_down example, the base case is when n is less than or equal to 0, which allows the function to stop calling itself and prevents infinite recursion.


#Example of indentifying the base case and recursive case in a different function:

def factorial(n):
    if n == 1:          # Base case
        return 1
    else:               # Recursive case
        return n * factorial(n - 1)

print(factorial(5))
#output: 120 - In this example, the function factorial calculates the factorial of a non-negative integer n. The base case is when n is equal to 1, where it returns 1. The recursive case is when n is greater than 1, where it returns n multiplied by the result of calling factorial with n-1. This allows the function to break down the problem into smaller subproblems until it reaches the base case, at which point it can return a result and stop the recursion. The output of this code will be 120, which is the factorial of 5 (5! = 5 * 4 * 3 * 2 * 1 = 120).

#Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. The Fibonacci sequence can be defined recursively as follows:
def fibonacci(n):
    if n <= 0:          # Base case for n = 0
        return 0
    elif n == 1:        # Base case for n = 1
        return 1
    else:               # Recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10))
#output: 55 - In this example, the function fibonacci calculates the nth Fibonacci number. The base cases are when n is less than or equal to 0, where it returns 0, and when n is equal to 1, where it returns 1. The recursive case is when n is greater than 1, where it returns the sum of the two preceding Fibonacci numbers by calling itself with n-1 and n-2. This allows the function to break down the problem into smaller subproblems until it reaches the base cases, at which point it can return a result and stop the recursion. The output of this code will be 55, which is the 10th Fibonacci number (F(10) = F(9) + F(8) = 34 + 21 = 55).

#Recursion with the list-

def sum_list(numbers):
    if len(numbers) == 0:  # Base case: empty list
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])  # Recursive case: sum first element and recurse on the rest of the list
my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))
#output: 15 - In this example, the function sum_list calculates the sum of a list of numbers. The base case is when the list is empty, where it returns 0. The recursive case is when the list is not empty, where it returns the first element of the list (numbers[0]) plus the result of calling sum_list on the rest of the list (numbers[1:]). This allows the function to break down the problem into smaller subproblems until it reaches the base case, at which point it can return a result and stop the recursion. The output of this code will be 15, which is the sum of the numbers in the list [1, 2, 3, 4, 5].


#finding the max value in a list using recursion-

def find_max(numbers):
    if len(numbers)==1:
        return numbers[0]
    else:
        max_of_rest=find_max(numbers[1:])
        return numbers[0] if numbers[0]>max_of_rest else max_of_rest
my_list=[3,5,2,8,1]
print(find_max(my_list))
#output: 8 - In this example, the function find_max calculates the maximum value in a list of numbers. The base case is when the list has only one element, where it returns that element as the maximum. The recursive case is when the list has more than one element, where it calls itself on the rest of the list (numbers[1:]) to find the maximum of the remaining elements. It then compares the first element of the list (numbers[0]) with the maximum of the rest and returns the larger of the two. This allows the function to break down the problem into smaller subproblems until it reaches the base case, at which point it can return a result and stop the recursion. The output of this code will be 8, which is the maximum value in the list [3, 5, 2, 8, 1].






















def find_max(numbers):
    # 🧠 This function finds the maximum number in a list using recursion

    # 🛑 Base Case:
    # If the list has only one element, return that element
    # because a single element is the maximum by default
    if len(numbers) == 1:
        return numbers[0]

    # 🔁 Recursive Case:
    # Call the same function on the rest of the list (excluding first element)
    # numbers[1:] means "all elements except the first one"
    max_of_rest = find_max(numbers[1:])

    # ⚖️ Compare:
    # Compare the first element with the maximum of the rest of the list
    # Return the larger value
    if numbers[0] > max_of_rest:
        return numbers[0]
    else:
        return max_of_rest


# 📌 Input list
my_list = [3, 5, 2, 8, 1]

# 🚀 Function call
print(find_max(my_list))   # Output: 8


# 🔍 How it works (step-by-step idea):
# find_max([3,5,2,8,1])
# → compare 3 with max([5,2,8,1])
# → compare 5 with max([2,8,1])
# → compare 2 with max([8,1])
# → compare 8 with max([1])
# → base case reached → return 1
# → compare 8 and 1 → return 8
# → compare 2 and 8 → return 8
# → compare 5 and 8 → return 8
# → compare 3 and 8 → return 8

