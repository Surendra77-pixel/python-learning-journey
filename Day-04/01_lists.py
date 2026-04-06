
#Lists - 

# a list is a collection of different data types which is ordered and modifiable(mutable means we can change the values in the list). It is defined using square brackets [] and can contain elements of different data types. and a list can be empty or it may have different data type items 

#where the list is used -
#1. To store multiple items in a single variable.   

#real world example of using list -
#1. Grocery List - A grocery list is a common example of a list in real life. It is a collection of items that you need to buy from the store. You can add items to the list, remove items from the list, and check off items as you purchase them. For example, your grocery list might include items like "milk", "bread", "eggs", and "fruits". You can easily modify this list as needed, making it a practical example of a list in everyday life.

#how to create a list in python- 
#1. using square brackets []
my_list = [1, "hello", 3.14, True]
print(my_list) #output: [1, 'hello', 3.14, True]

#2. using the list() constructor
my_list2 = list([1, "world", 2.71, False])
print(my_list2) #output: [1, 'world', 2.71, False]

#3.empty list
empty_list = []
print(empty_list) #output: []

#4.list with initial values and we use the len() function to get the length of the list:

fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway'] 

# Print the lists and its length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
#Fruits: ['banana', 'orange', 'mango', 'lemon']

print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
#Vegetables: ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
#Animal products: ['milk', 'meat', 'butter', 'yoghurt']

print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
#Web technologies: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']

print('Countries:', countries)
print('Number of countries:', len(countries))
#Countries: ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

#5. list  length - we can use the len() function to get the length of the list:
my_list=["surendra","manthri","20","hyderabad"]
print(len(my_list)) #output: 4

#6.type() function to check the type of the list:
my_list=["surendra","manthri","20","hyderabad"]
print(type(my_list)) #output: <class 'list'>

#7.list constructor - we can use the list() constructor to create a list from an iterable (like a string, tuple, or another list):
my_string = "hello"
my_list = list(my_string)
print(my_list) #output: ['h', 'e', 'l', 'l', 'o']

The_list=list(("Surendra","manthri","20","hyderabad"))
print(The_list) #output: ['Surendra', 'manthri', '20', 'hyderabad']

#8.creating the list with repeated elements using the multiplication operator:
repeated_list = [0] * 5
print(repeated_list) #output: [0, 0, 0, 0, 0]

user=["surendra","manthri","20","hyderabad"] *5
print(user) #output: ['surendra', 'manthri', '20', 'hyderabad', 'surendra', 'manthri', '20', 'hyderabad', 'surendra', 'manthri', '20', 'hyderabad', 'surendra', 'manthri', '20', 'hyderabad', 'surendra', 'manthri', '20', 'hyderabad'] 



#rules in lists -------------------------------------

#1. we use list to modify data because list is mutable

#2.dynamic operations - we can add, remove, or change items in a list after it has been created.

#3.list allows duplicate values - a list can contain duplicate values, meaning that the same value can appear multiple times in a list.

#4.list can store different data types - a list can contain elements of different data types, such as integers, strings, and booleans.

#supports indexing and slicing - you can access individual elements of a list using their index, and you can also slice a list to create a new list that contains a subset of the original elements.

#6.list are iterable - you can loop through the items in a list using a for loop or a while loop.

#7.list can be nested - you can create a list that contains other lists as its elements, allowing for the creation of complex data structures.

#8.supports membership testing - you can check if an item exists in a list using the in keyword, which returns True if the item is found in the list and False if it is not found.

#9.list cannot use index that is not present in the list - if you try to access an index that is out of range, it will raise an IndexError.

#Where the list is used in real life -

#1.student data - A list can be used to store student data in a school or university. Each student can be represented as a dictionary containing their name, age, grade, and other relevant information. The list can then be used to perform various operations such as sorting the students by their grades, filtering students based on their age, or calculating the average grade of the class.

#2.shopping cart - A list can be used to represent a shopping cart in an e-commerce application. Each item in the cart can be represented as a dictionary containing the product name, price, quantity, and other relevant information. The list can then be used to calculate the total cost of the items in the cart, apply discounts, or remove items from the cart.

#3.game development - A list can be used to store game objects in a video game. Each game object can be represented as a dictionary containing its position, velocity, and other relevant information. The list can then be used to update the position of each game object, check for collisions between objects, or render the objects on the screen. 

#4.web development - A list can be used to store data in a web application. For example, a list can be used to store user comments on a blog post, or to store the items in a user's shopping cart. The list can then be used to display the comments or the shopping cart items on the web page, or to perform operations such as sorting or filtering the data.

#5.data analysis - A list can be used to store data in a data analysis project. For example, a list can be used to store the values of a particular variable in a dataset, or to store the results of a calculation. The list can then be used to perform operations such as calculating the mean or median of the data, or to create visualizations such as histograms or scatter plots.

#6.machine learning - A list can be used to store data in a machine learning project. For example, a list can be used to store the features of a dataset, or to store the predicted values of a model. The list can then be used to perform operations such as calculating the accuracy of the model, or to create visualizations such as confusion matrices or ROC curves.

#7.file handling - A list can be used to store data read from a file. For example, a list can be used to store the lines of a text file, or to store the values of a CSV file. The list can then be used to perform operations such as searching for specific data in the file, or to create visualizations such as word clouds or bar charts.

#8.very importantly Api data - A list can be used to store data retrieved from an API (Application Programming Interface). For example, a list can be used to store the results of a search query, or to store the items in a user's social media feed. The list can then be used to perform operations such as filtering the data based on certain criteria, or to create visualizations such as timelines or graphs.

#finally list are used when -

#1.You have multiple items
#2.Data can change
#3.You need looping
#4.You need filtering

