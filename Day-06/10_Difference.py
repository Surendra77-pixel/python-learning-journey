#Diffeerence() method - 

# The difference() method returns a new set that contains the items that are present in the first set but not in the second set. Here is an example:
st1={"apple","banana","cherry"}
st2={"banana","cherry","date"}
st3=st1.difference(st2)
print(st3) #output: {'apple'} - The set st3 is created by taking the difference of st1 and st2 using the difference() method. The resulting set contains only the elements that are present in st1 but not in st2, which is "apple". Since sets do not maintain order, the output may appear in a different order than the original sets.   


#2- The difference() method can also be used with more than two sets. When multiple sets are provided, the method returns a new set that contains the items that are present in the first set but not in any of the other sets. Here is an example:
st1={"apple","banana","cherry"}
st2={"banana","cherry","date"}
st3={"date","elderberry","fig"}
st4=st1.difference(st2,st3)
print(st4) #output: {'apple'} - The set st4 is created by taking the difference of st1 with st2 and st3 using the difference() method. The resulting set contains only the elements that are present in st1 but not in either st2 or st3, which is "apple". Since sets do not maintain order, the output may appear in a different order than the original sets. Note that st2 and st3 remain unchanged after the operation.

#3- The difference() method can also be used with other iterables, such as lists or tuples. When an iterable is provided as an argument, the method returns a new set that contains the items that are present in the first set but not in the iterable. Here is an example:
st1={"apple","banana","cherry"}
st2=["banana","cherry","date"]
st3=st1.difference(st2)
print(st3) #output: {'apple'} - The set st3 is created by taking the difference of st1 with the list st2 using the difference() method. The resulting set contains only the elements that are present in st1 but not in st2, which is "apple". Since sets do not maintain order, the output may appear in a different order than the original set and list. Note that st1 and st2 remain unchanged after the operation.



#4- The difference() method does not modify the original set; it returns a new set with the difference. If you want to update the original set to keep only the items that are present in the first set but not in the second set, you can use the difference_update() method instead. 


#5- The difference() method is different from the symmetric_difference() method. The difference() method returns a set that contains the items that are present in the first set but not in the second set, while the symmetric_difference() method returns a set that contains the items that are present in either of the sets but not in both. Here is an example to illustrate the difference:


#6. "- operator - We can also use the - operator to find the difference of two sets. Here is an example:
st1={"apple","banana","cherry"}
st2={"banana","cherry","date"}
st3=st1 - st2
print(st3) #output: {'apple'} - The set st3 is created by using the - operator to find the difference of st1 and st2. The resulting set contains only the elements that are present in st1 but not in st2, which is "apple". Since sets do not maintain order, the output may appear in a different order than the original sets. Note that st1 and st2 remain unchanged after the operation.


#7. "-= operator - We can also use the -= operator to find the difference of two sets and update the original set. Here is an example:
st1={"apple","banana","cherry"}
st2={"banana","cherry","date"}
st1 -= st2
print(st1) #output: {'apple'} - The -= operator is used to update st1 by removing the items that are present in st2. After the operation, st1 contains only the elements that are present in st1 but not in st2, which is "apple". Since sets do not maintain order, the output may appear in a different order than the original sets. Note that st2 remains unchanged after the operation.


#8.
# The  difference can also be calculated using the - operator with more than two sets. When multiple sets are provided, the operator returns a new set that contains the items that are present in an odd number of the sets. Here is an example:
st1={"apple","banana","cherry"}
st2={"banana","cherry","date"}
st3={"date","elderberry","fig"}
st4=st1 - st2 - st3
print(st4) #output: {'apple'} - The set st4 is created by using the - operator to find the difference of st1 with st2 and st3. The resulting set contains only the elements that are present in st1 but not in either st2 or st3, which is "apple". Since sets do not maintain order, the output may appear in a different order than the original sets. Note that st1, st2, and st3 remain unchanged after the operation.


#8. The - operator and the -= operator can be only used with sets. If you try to use them with other iterables, such as lists or tuples, it will raise a TypeError.


