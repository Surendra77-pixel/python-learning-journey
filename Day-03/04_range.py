#range - generates a sequence of numbers. It can take one, two, or three arguments. The syntax of the range function is as follows:
#range(stop) - generates a sequence of numbers from 0 to stop-1.
#range(start, stop) - generates a sequence of numbers from start to stop-1.
#range(start, stop, step) - generates a sequence of numbers from start to stop-1, with a step of step.

#1.HERE WE PRINT THE NUMBERS FROM 0 TO 9 USING THE RANGE FUNCTION-
for i in range(10):
    print(i) #output: 0 1 2 3 4 5 6 7 8 9

#2.HERE WE PRINT THE NUMBERS FROM 1 TO 10 USING THE RANGE FUNCTION-
for i in range(1, 11):
    print(i) #output: 1 2 3 4 5 6 7 8 9 10

#3.HERE WE PRINT THE NUMBERS FROM 1 TO 10 WITH A STEP OF 2 USING THE RANGE FUNCTION-
for i in range(1, 11, 2):
    print(i) #output: 1 3 5 7 9

#4.HERE WE PRINT THE NUMBERS FROM 10 TO 1 IN REVERSE ORDER USING THE RANGE FUNCTION-
for i in range(10, 0, -1):
    print(i) #output: 10 9 8 7 6 5 4 3 2 1

    