# Asterisk (*) in Python

# The asterisk (*) is a versatile operator in Python that can be used in various contexts. Here are some common uses of the asterisk:

# 1. Unpacking Iterables: The asterisk can be used to unpack elements from an iterable (like a list or tuple) into individual variables. For example:
my_list = [1, 2, 3]
a, b, c = my_list
print(a)  # Output: 1


a=["Apple","Banana","Cherry","Orange","Mango"]
(green , yellow , red , *other)=a
print(green) #output: Apple
print(yellow) #output: Banana
print(red) #output: Cherry
print(other) #output: ['Orange', 'Mango'] - The asterisk (*) is used to unpack the remaining elements of the list a into the variable other. In this case, other will contain the elements "Orange" and "Mango" as a list, resulting in ['Orange', 'Mango'].


#if the astersik is added to another variable name than the last , python will assign values to the variables until the number of values left matches the number left with the asterisk variable. For example:
a=["Apple","Banana","Cherry","Orange","Mango"]
(green , *yellow , red)=a
print(green) #output: Apple
print(yellow) #output: ['Banana', 'Cherry', 'Orange'] - The asterisk (*) is used to unpack the middle elements of the list a into the variable yellow. In this case, yellow will contain the elements "Banana", "Cherry", and "Orange" as a list, resulting in ['Banana', 'Cherry', 'Orange'].
print(red) #output: Mango - The variable red is assigned the last element of the list a, which is "Mango", resulting in red being equal to "Mango".


