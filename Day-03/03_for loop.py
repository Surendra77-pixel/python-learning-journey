
#FOR LOOP IN PYTHON-
#The for loop is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each item in the sequence. The syntax of a for loop in Python is as follows:
#for variable in sequence:
    #block of code to be executed

#1.HERE WE PRINT THE NUMBERS FROM 1 TO 5 USING THE FOR LOOP-
for i in range(1, 6):
    print(i) #output: 1 2 3 4 5

#2.HERE WE PRINT THE NUMBERS FROM 10 TO 1 IN REVERSE ORDER USING THE FOR LOOP-
for num in range(10, 0, -1):
    print(num) #output: 10 9 8 7 6 5 4 3 2 1

#3.HERE WE PRINT THE ELEMENTS OF A LIST USING THE FOR LOOP-
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit) #output: apple banana cherry   

#4.HERE WE PRINT THE CHARACTERS OF A STRING USING THE FOR LOOP-
name = "surendra"
for char in name:
    print(char) #output: s u r e n d r a
    
#5.HERE WE PRINT NUMBERS OF A TUPLES USING THE FOR LOOP-
numbers = (1, 2, 3, 4, 5)
for number in numbers:
    print(number) #output: 1 2 3 4 5

#6.HERE WE PRINT THE LOOP THROUGH A DICTIONARY USING THE FOR LOOP-
person = {"name": "surendra", "age": 25, "city": "hyderabad"}
for key in person:
    print(key) #output: name age city
    print(person[key]) #output: surendra 25 hyderabad
    
#7.by using thr for loop making the numbers reverse:
for x in reversed(range(1,11)):
    print(x)
    #output- 10 9 8 7 6 5 4 3 2 1

#8.multiplication table 
#square number pattern

for i in range(11):
    print(i , "x",i,"=",i*i)
    #output:
    #0 x 0 = 0  
    #1 x 1 = 1
    #2 x 2 = 4
    #3 x 3 = 9
    #4 x 4 = 16
    #5 x 5 = 25
    #6 x 6 = 36
    #7 x 7 = 49
    #8 x 8 = 64
    #9 x 9 = 81
    #10 x 10 = 100

    
