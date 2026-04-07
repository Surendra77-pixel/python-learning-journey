
#symmetric difference - The symmetric difference of two sets is a set that contains all the elements that are in either of the sets, but not in their intersection. In other words, it includes elements that are in one set or the other, but not in both. The symmetric difference can be calculated using the symmetric_difference() method or the ^ operator. Here is an example:
st1={"apple","banana","cherry"}
st2={"banana","cherry","date"}
st3=st1.symmetric_difference(st2)
print(st3) #output: {'apple', 'date'} - The set st3 is created by taking the symmetric difference of st1 and st2 using the symmetric_difference() method. The resulting set contains the elements that are in either st1 or st2 but not in both, which are "apple" and "date". Since sets do not maintain order, the output may appear in a different order than the original sets. Note that st1 and st2 remain unchanged after the operation.


# The symmetric_difference() method can also be used with more than two sets. When multiple sets are provided, the method returns a new set that contains the items that are present in an odd number of the sets. Here is an example:
st1={"apple","banana","cherry"}
st2={"banana","cherry","date"}
st3={"date","elderberry","fig"}
st4=st1.symmetric_difference(st2).symmetric_difference(st3)
print(st4) #output: {'apple', 'elderberry', 'fig'} - The set st4 is created by taking the symmetric difference of st1 with st2 and st3 using the symmetric_difference() method. The resulting set contains the elements that are present in an odd number of the sets, which are "apple" (present in st1 only), "elderberry" (present in st3 only), and "fig" (present in st3 only). Since sets do not maintain order, the output may appear in a different order than the original sets. Note that st1, st2, and st3 remain unchanged after the operation.


# The symmetric_difference() method can also be used with other iterables, such as lists or tuples. When an iterable is provided as an argument, the method returns a new set that contains the items that are present in an odd number of the sets and the iterable. Here is an example:
st1={"apple","banana","cherry"}
st2=["banana","cherry","date"]
st3=st1.symmetric_difference(st2)
print(st3) #output: {'apple', 'date'} - The set st3 is created by taking the symmetric difference of st1 with the list st2 using the symmetric_difference() method. The resulting set contains the elements that are present in an odd number of the sets and the iterable, which are "apple" (present in st1 only) and "date" (present in st2 only). Since sets do not maintain order, the output may appear in a different order than the original set and list. Note that st1 and st2 remain unchanged after the operation.



# The symmetric_difference() method is different from the difference() method. The symmetric_difference() method returns a set that contains the items that are present in either of the sets but not in both, while the difference() method returns a set that contains the items that are present in the first set but not in the second set.


# The symmetric_difference() method is also different from the difference_update() method. The symmetric_difference() method returns a new set with the symmetric difference, while the difference_update() method updates the original set to keep only the items that are present in the first set but not in the second set. 


# 2.^-

# The symmetric difference can also be calculated using the ^ operator. Here is an example:

st1={"apple","banana","cherry"}
st2={"banana","cherry","date"}
st3=st1 ^ st2
print(st3) #output: {'apple', 'date'} - The set st3 is created by using the ^ operator to find the symmetric difference of st1 and st2. The resulting set contains the elements that are in either st1 or st2 but not in both, which are "apple" and "date". Since sets do not maintain order, the output may appear in a different order than the original sets. Note that st1 and st2 remain unchanged after the operation.


# The ^ operator can only be used with sets. If you try to use it with other iterables, such as lists or tuples, it will raise a TypeError. For example:
st1={"apple","banana","cherry"}
st2=["banana","cherry","date"]
# st3=st1 ^ st2 # This will raise a TypeError because the ^ operator only works with sets, and st2 is a list.

# The symmetric difference can also be calculated using the ^ operator with more than two sets. When multiple sets are provided, the operator returns a new set that contains the items that are present in an odd number of the sets. Here is an example:
st1={"apple","banana","cherry"}
st2={"banana","cherry","date"}
st3={"date","elderberry","fig"}
st4=st1 ^ st2 ^ st3
print(st4) #output: {'apple', 'elderberry', 'fig'} - The set st4 is created by using the ^ operator to find the symmetric difference of st1 with st2 and st3. The resulting set contains the elements that are present in an odd number of the sets, which are "apple" (present in st1 only), "elderberry" (present in st3 only), and "fig" (present in st3 only). Since sets do not maintain order, the output may appear in a different order than the original sets. Note that st1, st2, and st3 remain unchanged after the operation.

# The ^ operator is different from the - operator. The ^ operator returns a set that contains the items that are present in either of the sets but not in both, while the - operator returns a set that contains the items that are present in the first set but not in the second set. Here is an example to illustrate the difference:
st1={"apple","banana","cherry"}
st2={"banana","cherry","date"}
st3=st1 ^ st2
print(st3) #output: {'apple', 'date'} - The set st3 is created by using the ^ operator to find the symmetric difference of st1 and st2. The resulting set contains the elements that are in either st1 or st2 but not in both, which are "apple" and "date". Since sets do not maintain order, the output may appear in a different order than the original sets. Note that st1 and st2 remain unchanged after the operation.

st4=st1 - st2
print(st4) #output: {'apple'} - The set st4 is created by using the - operator to find the difference of st1 and st2. The resulting set contains only the elements that are present in st1 but not in st2, which is "apple". Since sets do not maintain order, the output may appear in a different order than the original sets. Note that st1 and st2 remain unchanged after the operation.


#(A\B) U (B\A) - The symmetric difference of two sets A and B can also be expressed as the union of the difference of A and B and the difference of B and A. In other words, it can be calculated as (A\B) U (B\A). Here is an example:
st1={"apple","banana","cherry"}
st2={"banana","cherry","date"}
st3=(st1 - st2).union(st2 - st1)
print(st3) #output: {'apple', 'date'} - The set st3 is created by first calculating the difference of st1 and st2 (st1 - st2) which results in {'apple'}, and then calculating the difference of st2 and st1 (st2 - st1) which results in {'date'}. Finally, the union of these two sets is taken using the union() method, resulting in a set that contains "apple" and "date". Since sets do not maintain order, the output may appear in a different order than the original sets. Note that st1 and st2 remain unchanged after the operation.