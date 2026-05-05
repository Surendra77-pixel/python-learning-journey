
#                Statistics module in Python

#1. The statistics module in Python is a built-in module that provides functions for calculating mathematical statistics of numeric data. It includes functions for calculating measures of central tendency (mean, median, mode), measures of variability (variance, standard deviation), and other statistical functions such as correlation and regression.

#2. To use the statistics module, you need to import it at the beginning of your Python script. This allows you to access the functions and variables defined in the statistics module.

import statistics

#3. Some common functions provided by the statistics module include:

#1.mean():

#The mean() function calculates the arithmetic mean (average) of a list of numbers. For example, statistics.mean([1, 2, 3, 4, 5]) will return 3.0.

mean_value = statistics.mean([1, 2, 3, 4, 5])

#2.median():

#The median() function calculates the median (middle value) of a list of numbers. For example, statistics.median([1, 2, 3, 4, 5]) will return 3.

median_value = statistics.median([1, 2, 3, 4, 5])


#3.mode():
#The mode() function calculates the mode (most common value) of a list of numbers. For example, statistics.mode([1, 2, 2, 3, 4]) will return 2.

mode_value = statistics.mode([1, 2, 2, 3, 4])


#4.variance():

#The variance() function calculates the variance of a list of numbers. For example, statistics.variance([1, 2, 3, 4, 5]) will return 2.5.

variance_value = statistics.variance([1, 2, 3, 4, 5])

#5.stdev():

#The stdev() function calculates the standard deviation of a list of numbers. For example, statistics.stdev([1, 2, 3, 4, 5]) will return 1.5811388300841898.

stdev_value = statistics.stdev([1, 2, 3, 4, 5])

