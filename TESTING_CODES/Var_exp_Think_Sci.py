 # source: https://openbookproject.net/thinkcs/python/english3e/variables_expressions_statements.html

 # Area = Area of Circle = πr2 

 # Firstly, we’ll do the four steps one at a time:


response = input("What is your radius? ")
r = float(response)
area = 3.14159 * r**2
print("The area is ", area)

# Firstly, we’ll do the four steps one at a time:

1
2
3
4
response = input("What is your radius? ")
r = float(response)
area = 3.14159 * r**2
print("The area is ", area)

# If we really wanted to be tricky, we could write it all in one statement:

1
print("The area is ", 3.14159*float(input("What is your radius?"))**2)

'''Such compact code may not be most understandable for humans, but it does illustrate how we can compose bigger chunks from our building blocks.

If you’re ever in doubt about whether to compose code or fragment it into smaller steps, 
try to make it as simple as you can for the human to follow. My choice would be the first case above, with four separate steps.'''

