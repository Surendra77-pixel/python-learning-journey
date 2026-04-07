
#Difference update -

# The difference_update() method removes the items from the first set that are also present in the second set. It modifies the original set and does not return a new set. Here is an example of how to use the difference_update() method:

st1={"apple","banana","cherry"}
st2={"banana","cherry","date"}
st1.difference_update(st2)
print(st1) #output: {'apple'} - The difference_update() method is called on the set st1 to update it by removing the items that are present in st2. After the operation, st1 contains only "apple", which is the item that is present in st1 but not in st2. Since sets do not maintain order, the output may appear in a different order than the original sets. Note that st2 remains unchanged after the operation.


# The difference_update() method can also be used with more than two sets. When multiple sets are provided, the method removes the items from the first set that are present in any of the other sets. Here is an example:
st1={"apple","banana","cherry"}
st2={"banana","cherry","date"}
st3={"date","elderberry","fig"}
st1.difference_update(st2,st3)
print(st1) #output: {'apple'} - The difference_update() method is called on st1 to update it by removing the items that are present in either st2 or st3. After the operation, st1 contains only "apple", which is the item that is present in st1 but not in either st2 or st3. Since sets do not maintain order, the output may appear in a different order than the original sets. Note that st2 and st3 remain unchanged after the operation.

# The difference_update() method can also be used with other iterables, such as lists or tuples. When an iterable is provided as an argument, the method removes the items from the first set that are present in the iterable. Here is an example:
st1={"apple","banana","cherry"}
st2=["banana","cherry","date"]
st1.difference_update(st2)
print(st1) #output: {'apple'} - The difference_update() method is called on st1 to update it by removing the items that are present in the list st2. After the operation, st1 contains only "apple", which is the item that is present in st1 but not in st2. Since sets do not maintain order, the output may appear in a different order than the original set and list. Note that st2 remains unchanged after the operation.


# The difference_update() method is different from the difference() method. The difference_update() method modifies the original set by removing the items that are present in the second set, while the difference() method returns a new set with the difference without modifying the original set. 

# The difference_update() method is also different from the symmetric_difference_update() method. The difference_update() method removes the items that are present in the second set from the first set, while the symmetric_difference_update() method updates the first set to contain only the items that are present in either of the sets but not in both. Here is an example to illustrate the difference:

