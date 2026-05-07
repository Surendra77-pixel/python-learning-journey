
#     collections module and types of collections in Python

#The collections module in Python provides a set of specialized container datatypes that are alternatives to the built-in types like list, dict, and tuple. These specialized containers are designed to provide additional functionality and performance benefits for specific use cases. Some of the most commonly used types of collections in the collections module include:

#1. namedtuple:

#The namedtuple is a factory function that generates a new subclass of tuple with named fields. It allows you to create simple classes that are immutable and can be accessed using dot notation. For example, you can create a namedtuple to represent a point in 2D space:
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p) #Output- Point(x=1, y=2)
#EXPLANATION- In the above code, we have imported the namedtuple function from the collections module and used it to create a new namedtuple class called Point with fields 'x' and 'y'. We then create an instance of the Point namedtuple with values (1, 2) and print it, which returns a string representation of the namedtuple with the field names and their corresponding values.


#2. deque:
#The deque (double-ended queue) is a list-like container that allows you to append and pop elements from both ends efficiently. It is implemented as a doubly linked list, which makes it ideal for use cases where you need to add or remove elements from both ends of the collection. For example, you can use a deque to implement a queue data structure:
from collections import deque
queue = deque()
queue.append('a')
queue.append('b')
queue.append('c')
print(queue) #Output- deque(['a', 'b', 'c'])
queue.popleft()
print(queue) #Output- deque(['b', 'c'])
#EXPLANATION- In the above code, we have imported the deque class from the collections module and created an instance of a deque called queue. We then append three elements ('a', 'b', and 'c') to the deque and print it, which returns a string representation of the deque with its elements. Next, we use the popleft() method to remove the leftmost element from the deque (which is 'a') and print the deque again, showing that 'a' has been removed and only 'b' and 'c' remain in the deque.


#3. Counter:
#The Counter is a subclass of dict that is used to count the occurrences of elements in a collection. It provides a convenient way to count the frequency of items in a list or other iterable. For example, you can use a Counter to count the occurrences of words in a list:
from collections import Counter
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_counts = Counter(words)
print(word_counts) #Output- Counter({'apple': 3, 'banana': 2, 'orange': 1})
#EXPLANATION- In the above code, we have imported the Counter class from the collections module and created a list of words. We then create a Counter object called word_counts by passing the list of words to the Counter constructor. The resulting word_counts object is a dictionary-like object that contains the count of each unique word in the list. When we print word_counts, it returns a string representation of the Counter object showing the count of each word, with 'apple' appearing 3 times, 'banana' appearing 2 times, and 'orange' appearing once.

#4. OrderedDict:
#The OrderedDict is a subclass of dict that maintains the order of keys as they were inserted. It is useful when you need to preserve the order of items in a dictionary. For example, you can use an OrderedDict to create a dictionary that maintains the order of keys:
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
print(ordered_dict) #Output- OrderedDict([('a', 1), ('b', 2), ('c', 3)])
#EXPLANATION- In the above code, we have imported the OrderedDict class from the collections module and created an instance of an OrderedDict called ordered_dict. We then add three key-value pairs to the ordered_dict in a specific order ('a': 1, 'b': 2, 'c': 3). When we print ordered_dict, it returns a string representation of the OrderedDict showing the key-value pairs in the order they were inserted.

#5. defaultdict:
#The defaultdict is a subclass of dict that provides a default value for keys that are not present in the dictionary. It allows you to specify a default factory function that will be called to provide a default value when a key is accessed that does not exist in the dictionary. For example, you can use a defaultdict to create a dictionary that returns a default value of 0 for keys that are not present:
from collections import defaultdict
default_dict = defaultdict(int)
default_dict['a'] += 1
default_dict['b'] += 2
print(default_dict) #Output- defaultdict(<class 'int'>, {'a': 1, 'b': 2})
#EXPLANATION- In the above code, we have imported the defaultdict class from the collections module and created an instance of a defaultdict called default_dict with a default factory function of int (which returns 0). We then increment the value of key 'a' by 1 and key 'b' by 2. Since 'a' and 'b' were not previously present in the dictionary, they are automatically initialized to 0 by the default factory function before being incremented. When we print default_dict, it returns a string representation of the defaultdict showing the key-value pairs with their respective counts.





