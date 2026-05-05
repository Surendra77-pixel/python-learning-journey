
#Range-

#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

#Syntax-

#range(start, stop, step)

#start: Optional. An integer number specifying at which position to start. Default is 0

#stop: Required. An integer number specifying at which position to stop (not included).

#step: Optional. An integer number specifying the incrementation. Default is 1

#The built-in range() function returns an immutable sequence of numbers between the given start integer to the stop integer. The given step integer value determines the increment (or decrement) for each number in the sequence. The range() function is commonly used for looping a specific number of times in for loops.

#Example-

x=range(5)
print(x)
print(list(x))
#Output-
#range(0, 5)
#[0, 1, 2, 3, 4]

#2.Calling the range() function with a single argument creates a sequence of numbers from 0 to the specified number (exclusive).
x=range(5)
print(list(x))
#Output-
#[0, 1, 2, 3, 4]

#3.Calling the range() function with two arguments creates a sequence of numbers from the first argument (inclusive) to the second argument (exclusive).
x=range(2, 5)
print(list(x))
#Output-
#[2, 3, 4]

#4.Calling the range() function with three arguments creates a sequence of numbers from the first argument (inclusive) to the second argument (exclusive), incrementing by the third argument.
x=range(2, 10, 2)
print(list(x))
#Output-
#[2, 4, 6, 8]

#5.Calling the range() function with a negative step creates a sequence of numbers in reverse order.
x=range(10, 0, -2)
print(list(x))
#Output-
#[10, 8, 6, 4, 2]

#6.The range() function can also be used to create a sequence of numbers with a specific step size, such as even or odd numbers.
x=range(0, 10, 2)
print(list(x))
#Output-
#[0, 2, 4, 6, 8]

x=range(1, 10, 2)
print(list(x))
#Output-
#[1, 3, 5, 7, 9]

#7.The range() function can also be used to create a sequence of numbers with a specific step size, such as multiples of a number.
x=range(0, 20, 5)
print(list(x))
#Output-
#[0, 5, 10, 15]


#8.The range() function can also be used to create a sequence of numbers with a specific step size, such as powers of a number.
x=range(1, 10, 2)
print(list(x))
#Output-
#[1, 3, 5, 7, 9]

#9.The range() function can also be used to create a sequence of numbers with a specific step size, such as Fibonacci numbers.
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
x=range(10)
print(list(fibonacci(10)))

#10.Ranges are often used in for loops to iterate over asequence of numbers

for i in range(5):
    print(i)
#Output-
#0
#1
#2
#3
#4

#11.The range() is also used in the  list comprehension to create a list of numbers.

squares = [x**2 for x in range(10)]
print(squares)
#Output-
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#12.slicing a list using range() function-

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sliced_list = my_list[range(2, 8)]
print(sliced_list)
#Output-
#[3, 4, 5, 6, 7, 8]

#13.slicing with the range()-

r=range(10)
print(r[2:8])
print(r[:2])
print(r[8:])
print(r[::2])
#Output-
#range(2, 8)
#range(0, 2)
#range(8, 10)
#range(0, 10, 2)
#explanation-
#In the above code, we have created a range object r with the range of 0 to 10. We have then sliced the range object using different slicing techniques. The first slice r[2:8] returns a new range object that starts from index 2 and ends at index 8 (exclusive). The second slice r[:2] returns a new range object that starts from the beginning of the range and ends at index 2 (exclusive). The third slice r[8:] returns a new range object that starts from index 8 and goes to the end of the range. The fourth slice r[::2] returns a new range object that includes every second element of the original range, starting from the first element.The main doubt all we get is why are we not geeting the list of numbers instead of range object, the answer is simple because the range() function returns a range object which is an immutable sequence of numbers. To get the list of numbers, we can convert the range object to a list using the list() function. For example, we can use list(r[2:8]) to get the list of numbers from index 2 to index 8 (exclusive).here is the example-
r=range(10)
print(list(r[2:8]))
#Output-
#[2, 3, 4, 5, 6, 7]

#14.Membership testing with range() function-

r=range(10)
print(5 in r)
print(15 in r)
#Output-
#True
#False

#15.The len() function can be used to get the number of elements in a range object.

r=range(10)
print(len(r))
#Output-
#10

