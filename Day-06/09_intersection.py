
#intersection of sets -

# The intersection of two sets is a new set that contains only the elements that are present in both sets. We can find the intersection of sets using the intersection() method or the & operator. Here are examples of each method:

#1.intersection() method - 

# The intersection() method returns a new set that contains only the elements that are present in both sets. Here is an example:
st1={"apple","banana","cherry"}
st2={"banana","cherry","date"}
st3=st1.intersection(st2)
print(st3) #output: {'banana', 'cherry'} - The set st3 is created by taking the intersection of st1 and st2 using the intersection() method. The resulting set contains only the elements that are present in both sets, which are "banana" and "cherry". Since sets do not maintain order, the output may appear in a different order than the original sets.

a={1,2,3,4}
b={3,4,5,6}
print(a.intersection(b)) 
#output: {3, 4} - The intersection of sets a and b is calculated using the intersection() method, resulting in a new set that contains only the elements that are present in both sets, which are 3 and 4. Since sets do not maintain order, the output may appear in a different order than the original sets.X

#2.& operator - 

# We can also use the & operator to find the intersection of two sets. Here is an example:
st1={"apple","banana","cherry"}
st2={"banana","cherry","date"}
st3=st1 & st2
print(st3) #output: {'banana', 'cherry'} - The set st3 is created by using the & operator to find the intersection of st1 and st2. The resulting set contains only the elements that are present in both sets, which are "banana" and "cherry". Since sets do not maintain order, the output may appear in a different order than the original sets.

#note - The object in the intersection method  can be any iterable, such as a list, tuple, or another set. For example:
st1={"apple","banana","cherry"}
st2=["banana","cherry","date"]
st3=st1.intersection(st2)
print(st3) #output: {'banana', 'cherry'} - The set st3 is created by taking the intersection of the set st1 and the list st2 using the intersection() method. The resulting set contains only the elements that are present in both the original set and the list, which are "banana" and "cherry". Since sets do not maintain order, the output may appear in a different order than the original set and list. Note that st1 and st2 remain unchanged after the operation.

a={1,2,3,4}
b=[3,4,5,6]
print(a.intersection(b)) #output: {3, 4} - The intersection of the set a and the list b is calculated using the intersection() method, resulting in a new set that contains only the elements that are present in both the original set and the list, which are 3 and 4. Since sets do not maintain order, the output may appear in a different order than the original set and list. Note that a and b remain unchanged after the operation.

#note - the & operator only works with sets, so if you try to use it with a list or another iterable, it will raise a TypeError. For example:

st1={"apple","banana","cherry"}
st2=["banana","cherry","date"]
# st3=st1 & st2 # This will raise a TypeError because the & operator only works with sets, and st2 is a list.

A = {1, 2, 3}
B = [2, 3, 4]

print(A & set(B)) #output: {2, 3} - The & operator is used to find the intersection of the set A and the set created from the list B. The resulting set contains only the elements that are present in both A and B, which are 2 and 3. Since sets do not maintain order, the output may appear in a different order than the original set and list. Note that A remains unchanged after the operation, while B is converted to a set for the intersection operation.


#The main difference between intersectiin and intersection_update is that the intersection() method returns a new set with the common elements, while the intersection_update() method updates the original set to keep only the common elements.