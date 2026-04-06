

#while through a tuple -----------------------------

#while loop can also be used to loop through the items in a tuple. Here is an example:

Thelist=("Surendra","manthri","20","hyderabad")
i=0
while i < len(Thelist):
    print(Thelist[i])
    i+=1
#output:
#Surendra
#manthri
#20
#hyderabad - The while loop uses an index variable i to access each item in the tuple Thelist. The loop continues as long as i is less than the length of the tuple (len(Thelist)). Inside the loop, we print the item at index i (Thelist[i]) and then increment i by 1 to move to the next index. Each item is printed on a new line, resulting in the output shown above.

#The length must be used in the while loop to ensure that we do not go out of range when accessing the items in the tuple. If we try to access an index that is greater than or equal to the length of the tuple, it will result in an IndexError. Therefore, using len(Thelist) in the while loop condition helps us avoid this error and ensures that we only access valid indices of the tuple.