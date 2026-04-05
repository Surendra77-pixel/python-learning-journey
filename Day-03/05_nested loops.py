#nested loops are loops inside loops. they are used to iterate over a sequence of sequences. the inner loop is executed for each iteration of the outer loop. here is an example of a nested loop that prints a pattern of stars:
for i in range(1, 6):
    for j in range(i):
        print("*", end="") #end="" is used to print the stars in the same line
    print() #this is used to move to the next line after printing the stars in each iteration of the outer loop. without this line all the stars will be printed in the same line.
#output:
#*
#**
#***
#****
#*****


#another example of a nested loop that prints a multiplication table:
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t") #end="\t" is used to print the numbers in a tabular format
    print() #this is used to move to the next line after printing the multiplication table for each number. without this line all the numbers will be printed in the same line. 
#output:
#1	2	3	4	5	6	7	8	9    10
#2	4	6	8	10	12	14	16	18    20
#3	6	9	12	15	18	21	24	27    30
#4	8	12	16	20	24	28	32	36    40
#5	10	15	20	25	30	35	40	45    50
#6	12	18	24	30	36	42	48	54    60
#7	14	21	28	35	42	49	56	63    70
#8	16	24	32	40	48	56	64	72    80
#9	18	27	36	45	54	63	72	81    90
#10	20	30	40	50	60	70	80	90    100

#example of a nested loop that prints a pattern of numbers:
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="") #end="" is used to print the numbers in the same line
    print() #this is used to move to the next line after printing the numbers in each iteration of the outer loop. without this line all the numbers will be printed in the same line.  
#output:
#1
#12
#123
#1234
#12345

#example of nested loop by using the lists:
adj=["red","big","tasty"]
fruits=["Apple","banana","cherry"]
for x in adj:
    for y in fruits:
        print(x,y)
#output:
#red Apple
#red banana
#red cherry
#big Apple
#big banana
#big cherry
#tasty Apple
#tasty banana
#tasty cherry

#explanation: In this code, we have two lists: adj and fruits. We use a nested loop to iterate through each element of the adj list and for each element in adj, we iterate through each element of the fruits list. Inside the inner loop, we print the current elements from both lists (x and y). As a result, we get all possible combinations of adjectives and fruits printed on separate lines.