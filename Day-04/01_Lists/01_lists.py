
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
print(my_list) #output: ['h', 'e', 'l', 'l',

The_list=list(("Surendra","manthri","20","hyderabad"))
print(The_list) #output: ['Surendra', 'manthri', '20', 'hyderabad']

#8.creating the list with repeated elements using the multiplication operator:
repeated_list = [0] * 5
print(repeated_list) #output: [0, 0, 0, 0, 0]

user=["surendra","manthri","20","hyderabad"] *5
print(user) #output: ['surendra', 'manthri', '20', 'hyderabad', 'surendra', 'manthri', '20', 'hyderabad', 'surendra', 'manthri', '20', 'hyderabad', 'surendra', 'manthri', '20', 'hyderabad', 'surendra', 'manthri', '20', 'hyderabad'] 




