 #FUNCTIONS -

# A function is a block of code which only runs when it is
called. You can pass data, known as parameters, into a function. A function can return
data as a result.


#when to use the functions:

#imagine you need to convert temperatures from fahrenheit to celsius several times in your program . without functions , you would have to write the same caluculation code repeatedly-

temp1=77
celsius1=(temp1-32)*5/9
print(celsius1)

temp1=95
celsius1=(temp1-32)*5/9
print(celsius1)

temp1=50
celsius1=(temp1-32)*5/9
print(celsius1)


#with functions, you can define a function to perform the conversion and then call it whenever needed, which makes your code cleaner and more efficient:

def fahrenheit_to_celsius(temp_f):
    return (temp_f - 32) * 5 / 9
print(fahrenheit_to_celsius(77)) #output: 25.0
print(fahrenheit_to_celsius(95)) #output: 35.0
print(fahrenheit_to_celsius(50)) #output: 10.0


