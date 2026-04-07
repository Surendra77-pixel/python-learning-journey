#intersection update() method - The intersection_update() method updates the set by keeping only the items that are present in both sets.


#The main difference between intersectiin and intersection_update is that the intersection() method returns a new set with the common elements, while the intersection_update() method updates the original set to keep only the common elements. Here is an example of how to use the intersection_update() method:

st1={"apple","banana","cherry"}
st2={"banana","cherry","date"}
st1.intersection_update(st2)
print(st1) #output: {'banana', 'cherry'} - The intersection_update() method is called on the set st1 to update it by keeping only the items that are present in both st1 and st2. After the operation, st1 contains only "banana" and "cherry", which are the common elements between the two sets. Since sets do not maintain order, the output may appear in a different order than the original sets. Note that st2 remains unchanged after the operation.

a={1,2,3,4}
b={3,4,5,6}
a.intersection_update(b)
print(a) #output: {3, 4} - The intersection_update() method is called on the set a to update it by keeping only the items that are present in both a and b. After the operation, a contains only 3 and 4, which are the common elements between the two sets. Since sets do not maintain order, the output may appear in a different order than the original sets. Note that b remains unchanged after the operation.



set1={"Apple",1,"banana",2,"cherry",3}
set2={True ,"banana",False,2,"date",3}
set1.intersection_update(set2)
print(set1) #output: {2, 3, 'banana'} - The intersection_update() method is called on set1 to update it by keeping only the items that are present in both set1 and set2. After the operation, set1 contains only 2, 3, and 'banana', which are the common elements between the two sets. Since sets do not maintain order, the output may appear in a different order than the original sets. Note that set2 remains unchanged after the operation.

#it accepts any iterable as an argument. For example:
set1={"Apple",1,"banana",2,"cherry",3}
list1=["banana",2,"date",3]
set1.intersection_update(list1)
print(set1) #output: {2, 3, 'banana'} - The intersection_update() method is called on set1 to update it by keeping only the items that are present in both set1 and the list list1. After the operation, set1 contains only 2, 3, and 'banana', which are the common elements between the original set and the list. Since sets do not maintain order, the output may appear in a different order than the original set and list. Note that list1 remains unchanged after the operation.

