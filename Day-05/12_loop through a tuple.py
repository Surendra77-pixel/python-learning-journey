
#1.loop through a tuple

#we can loop through the items in a tuple using a for loop. Here is an example:

Thelist=("Surendra","manthri","20","hyderabad")
for x in Thelist:
    print(x)
#output:
#Surendra
#manthri       -#The best method.
#20
#hyderabad - The for loop iterates through each item in the tuple Thelist and prints it. Each item is printed on a new line, resulting in the output shown above.


#2.loop through the index number -

# we can also loop through the index numbers of a tuple using the range() function and the len() function. Here is an example:

Thelist=("Surendra","manthri","20","hyderabad")
for i in range(len(Thelist)):
    print(Thelist[i])   
#output:
#Surendra
#manthri
#20
#hyderabad - The for loop iterates through the index numbers of the tuple Thelist using the range() function and the len() function. Inside the loop, we access each item in the tuple using its index (Thelist[i]) and print it. Each item is printed on a new line, resulting in the output shown above.
