
#set operators -

# Set operators are used to perform operations on sets, such as union, intersection, difference, and symmetric difference. Here are some common set operators in Python:

#1.| operator - The | operator is used to perform the union of two sets. It returns a new set that contains all the unique elements from both sets. Here is an example:
st1={"apple","banana","cherry"}
st2={"date","elderberry","fig"}
st3=st1 | st2
print(st3) #output: {'apple', 'banana', 'cherry', 'date','elderberry', 'fig'} 

#2.& operator - The & operator is used to perform the intersection of two sets. It returns a new set that contains only the elements that are present in both sets. Here is an example:
st1={"apple","banana","cherry"}
st2={"banana","cherry","date"}
st3=st1 & st2
print(st3) #output: {'banana', 'cherry'} 


#3.^ operator - The ^ operator is used to perform the symmetric difference of two sets. It returns a new set that contains the elements that are in either of the sets but not in both. Here is an example:
st1={"apple","banana","cherry"}
st2={"banana","cherry","date"}
st3=st1 ^ st2
print(st3) #output: {'apple', 'date'}

