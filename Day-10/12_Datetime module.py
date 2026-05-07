
#            Datetime module

#The datetime module provides classes for manipulating dates and times. It allows you to work with dates and times in both simple and complex ways. For example, we can use the datetime.now() function to get the current date and time.

import datetime
current_datetime = datetime.datetime.now()
print(current_datetime) #Output- 2024-06-30 12:34:56.789012
#explanation- In the above code, we have imported the datetime module and used the now() function to get the current date and time, which returns a datetime object representing the current date and time.

#The datetime module also provides other classes such as date, time, timedelta, and more. For example, we can use the date class to create a date object representing a specific date.
from datetime import date
my_date = date(2024, 6, 30)
print(my_date) #Output- 2024-06-30
#explanation- In the above code, we have imported the date class from the datetime module and created a date object representing June 30, 2024. The date object is then printed, which returns the date in the format YYYY-MM-DD.

#We can also perform operations on datetime objects. For example, we can use the timedelta class to add or subtract a certain amount of time from a datetime object.
from datetime import timedelta
current_datetime = datetime.datetime.now()
new_datetime = current_datetime + timedelta(days=7)
print(new_datetime) #Output- Current date and time plus 7 days
#explanation- In the above code, we have imported the timedelta class from the datetime module and used it to add 7 days to the current date and time. The new datetime object is then printed, which returns the date and time that is 7 days in the future.

#The datetime module also provides functions for formatting and parsing dates and times. For example, we can use the strftime() method to format a datetime object as a string.
current_datetime = datetime.datetime.now() 
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime) #Output- Current date and time in the format YYYY-MM-DD HH:MM:SS
#explanation- In the above code, we have used the strftime() method to format the current date and time as a string in the format YYYY-MM-DD HH:MM:SS. The formatted datetime string is then printed.


#We can also use the strptime() method to parse a string into a datetime object.
date_string = "2024-06-30 12:34:56" 
parsed_datetime = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(parsed_datetime) #Output- 2024-06-30 12:34:56
#explanation- In the above code, we have used the strptime() method to parse a string representing a date and time into a datetime object. The date_string is in the format YYYY-MM-DD HH:MM:SS, and the resulting parsed_datetime object represents that specific date and time.

#Types of datetime objects:

#1. datetime: This class represents both date and time. It includes attributes for year, month, day, hour, minute, second, and microsecond.

#2. date: This class represents a date (year, month, and day) without time information.

#3. time: This class represents a time (hour, minute, second, and microsecond) without date information.

#4. timedelta: This class represents a duration, which is the difference between two dates or times. It can be used to perform arithmetic operations on datetime objects, such as adding or subtracting a certain amount of time.

#1. datetime: This class represents both date and time. It includes attributes for year, month, day, hour, minute, second, and microsecond.
import datetime
current_datetime = datetime.datetime.now()  
print(current_datetime) #Output- 2024-06-30 12:34:56.789012
#explanation- In the above code, we have imported the datetime module and used the now() function to get the current date and time, which returns a datetime object representing the current date and time.

#2. date: This class represents a date (year, month, and day) without time information.
from datetime import date
my_date = date(2024, 6, 30)
print(my_date) #Output- 2024-06-30
#explanation- In the above code, we have imported the date class from the datetime module and created a date object representing June 30, 2024. The date object is then printed, which returns the date in the format YYYY-MM-DD.


#3. time: This class represents a time (hour, minute, second, and microsecond) without date information.
from datetime import time
my_time = time(12, 34, 56)
print(my_time) #Output- 12:34:56
#explanation- In the above code, we have imported the time class from the datetime module and created a time object representing 12:34:56. The time object is then printed, which returns the time in the format HH:MM:SS.


#4. timedelta: This class represents a duration, which is the difference between two dates or times. It can be used to perform arithmetic operations on datetime objects, such as adding or subtracting a certain amount of time.
from datetime import timedelta
current_datetime = datetime.datetime.now()
new_datetime = current_datetime + timedelta(days=7)
print(new_datetime) #Output- Current date and time plus 7 days
#explanation- In the above code, we have imported the timedelta class from the datetime module and used it to add 7 days to the current date and time. The new datetime object is then printed, which returns the date and time that is 7 days in the future.

