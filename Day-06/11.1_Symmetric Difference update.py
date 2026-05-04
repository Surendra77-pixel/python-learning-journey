
#symmetric difference update() method - 

# The symmetric_difference_update() method updates the set by keeping only the items that are present in either of the sets but not in both sets. Here is an example of how to use the symmetric_difference_update() method:

st1={"apple","banana","cherry"}
st2={"banana","cherry","date"}
st1.symmetric_difference_update(st2)
print(st1) #output: {'apple', 'date'} - The symmetric_difference_update() method is called on the set st1 to update it by keeping only the items that are present in either st1 or st2 but not in both. After the operation, st1 contains "apple" (present in st1 only) and "date" (present in st2 only). Since sets do not maintain order, the output may appear in a different order than the original sets. Note that st2 remains unchanged after the operation.


# The symmetric_difference_update() method can also be used with more than two sets. When multiple sets are provided, the method updates the first set to contain only the items that are present in an odd number of the sets. Here is an example:
st1={"apple","banana","cherry"}
st2={"banana","cherry","date"}
st3={"date","elderberry","fig"}
st1.symmetric_difference_update(st2)
st1.symmetric_difference_update(st3)
print(st1) #output: {'apple', 'elderberry', 'fig'} - The set st1 is updated by first taking the symmetric difference with st2 and then taking the symmetric difference of the result with st3 using the symmetric_difference_update() method. After the operations, st1 contains "apple" (present in st1 only), "elderberry" (present in st3 only), and "fig" (present in st3 only). Since sets do not maintain order, the output may appear in a different order than the original sets. Note that st2 and st3 remain unchanged after the operation.


# The symmetric_difference_update() method can also be used with other iterables, such as lists or tuples. When an iterable is provided as an argument, the method updates the set to contain only the items that are present in an odd number of the sets and the iterable. Here is an example:
st1={"apple","banana","cherry"}
st2=["banana","cherry","date"]
st1.symmetric_difference_update(st2)
print(st1) #output: {'apple', 'date'} - The set st1 is updated by taking the symmetric difference with the list st2 using the symmetric_difference_update() method. After the operation, st1 contains "apple" (present in st1 only) and "date" (present in st2 only). Since sets do not maintain order, the output may appear in a different order than the original set and list. Note that st2 remains unchanged after the operation.


# The symmetric_difference_update() method is different from the symmetric_difference() method. The symmetric_difference_update() method modifies the original set to keep only the items that are present in either of the sets but not in both, while the symmetric_difference() method returns a new set with the symmetric difference without modifying the original set.


