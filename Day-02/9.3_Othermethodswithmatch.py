#the match with the if statement:

month=5
day=5
match day:
    case 1 | 21 | 31:
        suffix="st"
    case 5 | 22 if month == 5:
        suffix="nd"
        suffix="5th"
    case 3 | 23:
        suffix="rd"
    case _:
        suffix="th"
print(f"{day}{suffix} of month {month}{suffix}") #output: 5th of month 5th


#suffix -A suffix is a group of letters added to the end of a word to change its meaning or function. in the context of the match statement, a suffix is used to indicate the ordinal number of a day in a month. for example, the suffix "st" is used for the 1st, 21st, and 31st days of a month, while the suffix "nd" is used for the 2nd and 22nd days of a month. the suffix "rd" is used for the 3rd and 23rd days of a month, and the suffix "th" is used for all other days of a month.


# Match-Case with Logical Operators In Python match-case, you cannot directly use and, or, not like in if BUT you can achieve similar behavior using:
 
#using and-

age = int(input("Enter age: "))
status = input("Enter status (student/worker): ")

match (age, status):
    case (a, s) if a > 18 and s == "student":
        print("Eligible student adult")
    case _:
        print("Not eligible")
        #output:
        #Enter age: 20
        #Enter status (student/worker): student
        #Eligible student adult
        #explanation: In this example, we are using a tuple (age, status) to match against the cases. The first case checks if the age is greater than 18 and the status is "student". If both conditions are true, it prints "Eligible student adult". The second case is the default case that matches anything that doesn't match the first case, and it prints "Not eligible".  

#example 2: using or-

num = int(input("Enter a number: "))
match num:
    case n if n == 0 or n == 1:
        print("Binary digit")
    case _:
        print("Not binary")
        #output:
        #Enter a number: 1  
        #Binary digit
        #explanation: In this example, we are using a single variable num to match against the cases. The first case checks if num is either 0 or 1 using the logical operator or. If num is 0 or 1, it prints "Binary digit". The second case is the default case that matches anything that doesn't match the first case, and it prints "Not binary".

#using not -

x = int(input("Enter number: "))

match x:
    case n if not n > 0:
        print("Non-positive number")
    case _:
        print("Positive number")
        #output:
        #Enter number: -5   
        #Non-positive number
        #explanation: In this example, we are using a single variable x to match against the cases. The first case checks if x is not greater than 0 using the logical operator not. If x is not greater than 0, it prints "Non-positive number". The second case is the default case that matches anything that doesn't match the first case, and it prints "Positive number".


#Match-Case with Membership Operators (in, not in) -

#- very useful when you want to check if a value is present in a collection (like a list, tuple, or set) within a match-case statement.

#using in operator:
fruit = input("Enter fruit: ")

match fruit:
    case f if f in ["apple", "banana", "mango"]:
        print("This is a common fruit")
    case _:
        print("Unknown fruit")
        #output:
        #Enter fruit: apple 
        #This is a common fruit
        #explanation: In this example, we are using a single variable fruit to match against the cases. The first case checks if fruit is in the list ["apple", "banana", "mango"] using the membership operator in. If fruit is one of those three fruits, it prints "This is a common fruit". The second case is the default case that matches anything that doesn't match the first case, and it prints "Unknown fruit".


#exmple 2: using not in operator:
char = input("Enter a character: ")

match char:
    case c if c not in "aeiou":
        print("Consonant")
    case _:
        print("Vowel")
        #output:
        #Enter a character: b
        #Consonant
        #explanation: In this example, we are using a single variable char to match against the cases. The first case checks if char is not in the string "aeiou" using the membership operator not in. If char is not a vowel (i.e., it is a consonant), it prints "Consonant". The second case is the default case that matches anything that doesn't match the first case, and it prints "Vowel".


#example  membership operator with numbers:
num = int(input("Enter number: "))

match num:
    case n if n in range(1, 11):
        print("Between 1 and 10")
    case _:
        print("Out of range")
        #output:
        #Enter number: 5
        #Between 1 and 10
        #explanation: In this example, we are using a single variable num to match against the cases. The first case checks if num is in the range from 1 to 10 (inclusive) using the membership operator in with the range function. If num is between 1 and 10, it prints "Between 1 and 10". The second case is the default case that matches anything that doesn't match the first case, and it prints "Out of range".

