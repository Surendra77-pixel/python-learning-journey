
#                    Iterators in Python

#In Python, an iterator is an object that implements the iterator protocol, which consists of the __iter__() and __next__() methods. An iterator allows you to traverse through all the elements of a collection, such as a list or a tuple, one at a time.

#In simple words we can like the iterator is the object that actually reads the items one by one 


#An iterable is an object that contains number of values 

#An iterator is an object that can be iterated upon,meaning that you can traverse through all the values. Technically, an iterator is any object which implements the __iter__() and __next__() methods.

#Iterator vs Iterable-

#1. An iterable is an object that can be iterated over, while an iterator is an object that can be used to iterate over an iterable.for example, a list is an iterable, while an iterator is an object that can be used to iterate over the elements of the list.list , tuple , strings , set , dictionary are all iterables in Python, while an iterator is an object that can be used to traverse through the elements of these iterables.

#in simple we can say that the iterable is known as the collection of the data and the iterator is the object that can be used to traverse through the elements of the collection one by one.

my_list = [10, 20, 30]

for item in my_list:
    print(item)
#Output-
#10
#20
#30
#In this example, my_list is an iterable, and the for loop creates an iterator to traverse through the elements of the list.

#2. An iterable can be converted into an iterator using the iter() function, while an iterator can be used to get the next element using the next() function. For example:
my_list = [10, 20, 30]
my_iterator = iter(my_list)  # Convert the list into an iterator
print(next(my_iterator))  # Output: 10
print(next(my_iterator))  # Output: 20
print(next(my_iterator))  # Output: 30
#In this example, we first convert the list my_list into an iterator using the iter() function. We then use the next() function to get the next element from the iterator, which returns 10, 20, and 30 in sequence.

#3.What is an iterator in Python?

#An iterator in Python is an object that implements the iterator protocol, which consists of the __iter__() and __next__() methods. An iterator allows you to traverse through all the elements of a collection, such as a list or a tuple, one at a time. The __iter__() method returns the iterator object itself, while the __next__() method returns the next element in the sequence. When there are no more elements to return, the __next__() method raises a StopIteration exception to signal that the iteration is complete. Iterators are commonly used in for loops and other constructs that require sequential access to elements in a collection.

my_list = [10, 20, 30]

it = iter(my_list)  # convert iterable → iterator

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30

#At here the it is an iterator object that is created from the list my_list using the iter() function. We can use the next() function to get the next element from the iterator, which returns 10, 20, and 30 in sequence. When there are no more elements to return, the next() function will raise a StopIteration exception to signal that the iteration is complete.

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
#Output-
#b
#a
#n
#a
#n
#a

#1.looping through an iterator using a for loop-

my_list = [10, 20, 30]
for item in my_list:
    print(item)
#Output-
#10
#20
#30
#In this example, we are using a for loop to iterate through the elements of the list my_list. The for loop automatically creates an iterator from the list and retrieves each element one by one until it reaches the end of the list.

#list , tupes , boolean , set , dictionary are all iterables in Python, while an iterator is an object that can be used to traverse through the elements of these iterables.

#How to stop the iteration of an iterator?

#When there are no more elements to return, the __next__() method of an iterator raises a StopIteration exception to signal that the iteration is complete. To stop the iteration of an iterator, you can catch this exception using a try-except block. For example:

my_list = [10, 20, 30]
my_iterator = iter(my_list)  # Convert the list into an iterator
while True:
    try:
        item = next(my_iterator)  # Get the next element from the iterator
        print(item)
    except StopIteration:
        break  # Exit the loop when there are no more elements to iterate

#In this example, we use a while loop to continuously call the next() function on the iterator my_iterator. When there are no more elements to return, the next() function raises a StopIteration exception, which we catch in the except block. We then break out of the loop to stop the iteration.   

