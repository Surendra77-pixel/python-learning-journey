
#3 Iterable -------------------

#an iterable can be any iterable object, such as a list, tuple, string, or even a generator. An iterable is an object that can be looped over (iterated) using a for loop or any other iteration context.

#simpily we can say that an iterable is an object that contains values and allows you to access them one at a time. It is a fundamental concept in Python and is used in many different contexts, such as loops, comprehensions, and functions that take iterables as arguments.



#1. using a for loop to iterate through an iterable - You can use a for loop to iterate through the items of an iterable. The for loop will execute a block of code for each item in the iterable.
fruits = ["banana", "apple", "cherry"]
for fruit in fruits:
    print(fruit)
#output:
#banana
#apple
#cherry


newlist = [x for x in range(10)] 
print(newlist) #output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#now we see with the condition-

newlist = [x for x in range(10) if x % 2 == 0]
print(newlist) #output: [0, 2, 4, 6, 8]



