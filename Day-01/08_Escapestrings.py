#escape strings- the escape strings is used to make the form of the difference in the sentence there are there are few types of teh escape strings

#\'-single quote is the one which we get the single quote in the praragraph 
a="This is the \' python \'code "
print(a) #Output: This is the ' python 'code - The escape sequence \' allows us to include a single quote within the string without causing a syntax error, resulting in the output "This is the ' python 'code".

#\"-double quote is the one which we get the double quote in the praragraph
b="This is the \" python \"code "   
print(b) #Output: This is the " python "code - The escape sequence \" allows us to include a double quote within the string without causing a syntax error, resulting in the output "This is the " python "code".

#\\- backslash is the one which we get the backslash in the praragraph
c="This is the \\ python \\code "
print(c) #Output: This is the \ python \code - The escape sequence \\ allows us to include a backslash within the string without causing a syntax error, resulting in the output "This is the \ python \code".

#\n- new line is the one which we get the new line in the praragraph
d="This is the python code \n which is used for the programming"
print(d) #Output: This is the python code
          # which is used for the programming - The escape sequence \n allows us to include a new line within the string, resulting in the output being split into two lines: "This is the python code" and " which is used for the programming".

#\t- tab is the one which we get the tab in the praragraph
e="This is the python code \t which is used for the programming"
print(e) #Output: This is the python code
          # which is used for the programming - The escape sequence \t allows us to include a tab within the string, resulting in the output being indented: "This is the python code" and " which is used for the programming".    

#\b- backspace is the one which we get the backspace in the praragraph
f="This is the python code \b which is used for the programming"
print(f) #Output: This is the python code which is used for the programming - The escape sequence \b allows us to include a backspace within the string, which removes the character before it, resulting in the output "This is the python code which is used for the programming".

#skipping characters while slicing the string
g="This is the python code which is used for the programming"
print(g[0:10]) #Output: This is th - The slicing operation g[0:10] retrieves the characters from index 0 to index 9 (10 is exclusive) of the string g, resulting in the output "This is th"..