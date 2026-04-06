
#conditions-----------------------

#The conditions is like a filter that only accepts the items that evaluate to True. 

fruits= ["banana", "apple", "cherry", "date", "fig"]
newlist=[x for x in fruits if "a" in x]
print(newlist) #output: ['banana', 'apple', 'date']


fruits= ["banana", "apple", "cherry", "date", "fig"]
newlist=[x for x in fruits if x!="banana"]
print(newlist) #output: ['apple', 'cherry', 'date', 'fig']

fruits= ["banana", "apple", "cherry", "date", "fig"]
newlist=[x for x in fruits if x!="banana" and x!="apple"]
print(newlist) #output: ['cherry', 'date', 'fig']

