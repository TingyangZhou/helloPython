#single line comment
'''
This is a multi-line comment
I can keep typing
Everyghing is a comment

'''

#I/O
print("Hello") #single quotes
print('Hello') #Double quotes
print("Greg's Notebook") # if you have single quotes within the quotes, you should use double quotes

#Objects/variables
#store the number 9 in an Object
x=9

#store a name - Tom
# store a letter -u
# store a decimal value -7.2

fname = "Tom"
my_letter = "u"
val = 7.2

# what will happen?
x = "Tom"
x= my_letter
x = 7.2
x = 7

x += 1 
print(x)
x = x+1
print(x)

# whitespace matters! 
#new ine for each instruction
#"Tab" character is used for code block
if True:
    x += 1 
    print("Hello")
    print("goodbye")
    
    
# I/O - formatted strings
a = 1 
b = 2

#print all 3 values a, b, x
print(a)
print(b)
print(x)
print(a, b, x)
# print "The values of a, b and x are 1, 2 and 7."
print("The values of a, b and x are", a,",", b,"and",x)
# Alternative better way - use an f-string, you get the value of the varibles stored in {}
print(f"The values of a, b and x are {a}, {b}, and {x}.")
# Expressions work as well
print(f"If we add a and b, we get {a+b}")

# Can we use other data types?
print(f"Here are some objects: {a}, {fname}, and {my_letter}")

#Take input from console
x = input("Please enter a number: ")
#check the data type of x
print(type(x))

# change a string to a number?
# Typecasting
x  = int(x)
print(x+1)

# GOAL: Take input from console, cast to integer, save as "a"
a=int(input("Please enter a number: "))
print(type(a))
print(a)