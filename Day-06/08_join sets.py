
#join sets-
# we can join two sets using the union() method or the update() method. Here are examples of each method:

#1.union() method - 

# The union() method returns a new set that contains all the unique elements from both sets. Here is an example:
st1={"apple","banana","cherry"}
st2={"date","elderberry","fig"}
st3=st1.union(st2)
print(st3) #output: {'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig'} - The set st3 is created by taking the union of st1 and st2 using the union() method. The resulting set contains all the unique elements from both sets, and since sets do not maintain order, the output may appear in a different order than the original sets.

a={1,2,3,4}
b={3,4,5,6}
print(a.union(b)) #output: {1, 2, 3, 4, 5, 6} - The union of sets a and b is calculated using the union() method, resulting in a new set that contains all the unique elements from both sets, which are 1, 2, 3, 4, 5, and 6. Since sets do not maintain order, the output may appear in a different order than the original sets. 


#2.update() method - 

# The update() method adds all the unique elements from one set to another set. Here is an example:
st1={"apple","banana","cherry"}
st2={"date","elderberry","fig"}
st1.update(st2)
print(st1) #output: {'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig'} - The update() method is called on the set st1 to add all the unique elements from st2. After the update, st1 contains all the unique elements from both sets, and since sets do not maintain order, the output may appear in a different order than the original sets. Note that st2 remains unchanged after the update operation.  


#note - The object in the update and union methods can be any iterable, such as a list, tuple, or another set. For example:

st1={"apple","banana","cherry"}
st2=["date","elderberry","fig"]
st1.update(st2)
print(st1) #output: {'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig'} - The update() method is called on the set st1 to add all the unique elements from the list st2. After the update, st1 contains all the unique elements from both the original set and the list, and since sets do not maintain order, the output may appear in a different order than the original set and list. Note that st2 remains unchanged after the update operation.

#example of using the union method with a list -
st1={"apple","banana","cherry"}
st2=["date","elderberry","fig"]
st3=st1.union(st2)
print(st3) #output: {'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig'} - The set st3 is created by taking the union of the set st1 and the list st2 using the union() method. The resulting set contains all the unique elements from both the original set and the list, and since sets do not maintain order, the output may appear in a different order than the original set and list. Note that st1 and st2 remain unchanged after the union operation.



#3.by using the | operator - 

# we can also use the | operator to join two sets. Here is an example:
st1={"apple","banana","cherry"}
st2={"date","elderberry","fig"}
st3=st1 | st2
print(st3) #output: {'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig'} - The set st3 is created by using the | operator to join st1 and st2. The resulting set contains all the unique elements from both sets, and since sets do not maintain order, the output may appear in a different order than the original sets.


#4.by using the |= operator - 

# we can also use the |= operator to join two sets. Here is an example:
st1={"apple","banana","cherry"}
st2={"date","elderberry","fig"}
st1 |= st2
print(st1) #output: {'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig'} - The |= operator is used to update st1 by adding all the unique elements from st2. After the operation, st1 contains all the unique elements from both sets, and since sets do not maintain order, the output may appear in a different order than the original sets. Note that st2 remains unchanged after the operation.

#5.joining muitiple sets - 

# we can also join multiple sets together using the union() method or the | operator. Here is an example:
st1={"apple","banana","cherry"}
st2={"date","elderberry","fig"}
st3={"grape","honeydew","kiwi"}
st4=st1.union(st2,st3)
print(st4) #output: {'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi'} - The union() method is used to join multiple sets together. The resulting set contains all the unique elements from all the sets, and since sets do not maintain order, the output may appear in a different order than the original sets.


#when using the | operator to join multiple sets, you can chain the operators together. Here is an example:
st1={"apple","banana","cherry"}
st2={"date","elderberry","fig"}
st3={"grape","honeydew","kiwi"}
st4=st1 | st2 | st3
print(st4) #output: {'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi'} - The | operator is used to join multiple sets together by chaining the operators. The resulting set contains all the unique elements from all the sets, and since sets do not maintain order, the output may appear in a different order than the original sets.   



#note - the | is only allows you to join sets together, so if you try to use the | operator to join a set with a list or a tuple, it will raise a TypeError because the | operator is not designed to work with non-set iterables. For example:
st1={"apple","banana","cherry"}
st2=["date","elderberry","fig"]
#st1|=st2 # This will raise a TypeError because the | operator cannot be used to join a set with a list. The | operator is specifically designed for set operations, and it expects both operands to be sets. If you want to join a set with a list or a tuple, you should use the union() method instead, as shown in the previous examples.



#The difference between union and update method - The union() method returns a new set that contains all the unique elements from both sets, while the update() method modifies the original set by adding all the unique elements from another set. The union() method does not change the original sets, while the update() method changes the original set that it is called on. For example:
st1={"apple","banana","cherry"}                     
st2={"date","elderberry","fig"}
st3=st1.union(st2)
print(st1) #output: {'apple', 'banana', 'cherry'} - The union() method is called on st1 to create a new set st3 that contains all the unique elements from both st1 and st2. After the operation, st1 remains unchanged, and when printed, it still contains only "apple", "banana", and "cherry".

st1={"apple","banana","cherry"}
st2={"date","elderberry","fig"}
st1.update(st2)
print(st1) #output: {'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig'} - The update() method is called on st1 to add all the unique elements from st2. After the operation, st1 is modified to include all the unique elements from both sets, and when printed, it contains "apple", "banana", "cherry", "date", "elderberry", and "fig". Note that st2 remains unchanged after the operation.

