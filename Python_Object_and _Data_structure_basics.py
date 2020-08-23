# Data Types
# ==========
# int -- Whole numbers, ex: 3, 10, 200
# float -- Numbers with decimal points, ex: 3.5, 100.0, 50.4
# str -- Ordered sequence of characters, ex: "hello", 'sammy', "2000"
# list -- Ordered sequence of objects, ex: [10, "hello", 200.3]
# dict -- Unordered key:value pairs, ex: {"mykey":"value", "name":"value"}
# tuple -- Ordered immutable sequence of Objects, ex: (10, "hello", 200.3)
# set -- Unordered collection of unique objects, ex: {"a","b"}
# bool -- Logical value indicating True or False

# Numbers
# =======
2 + 3
3 - 2
4 / 2
3 * 2

5 % 2  # Mod operator to get remainder
2 ** 3  # power (2 to the power of 3)

# Arithmetic expressions
# ======================
2 + 10 * 10 + 3  # This will result into 105
(2 + 10) * (10 + 3)  # This will result into 156

# Variable assignments
# ====================
my_dog = 2

# Rules for Variable names
# 1) Variable name cannot start with number
# 2) No spaces allowed in the name, use "_" instead
# 3) can't use any of the below symbols ==> :'",<>/?|\()!@#$%^&*~-+
# 4) Its considered best practice that names should be in lower case
# 5) Avoid using words that has special meaning in python like "str" or "list"

# Python dynamically typed language. that means you can assign same variable name to two different data types. This is
# a advantage of python.
# ex:

my_dog = ['dog1', 'dog2']  # So here we have assigned my_dog to other data type which is list here.

# Pros of dynamic typing
# 1) Very easy to work with
# 2) Faster development time
# cons of dynamic typing
# 1) may result in bugs for unexpected data types
# 2) you need to be aware of type() function to check the current data type of a variable before using it.

a = 5
print(a)

a = 10  # Here we are reassigning the new value to same variable.
print(a)

a = a + a  # Here we are reassigning value fo a with reference to a itself.
print(a)

# now lets apply "type()" function on above variable to check its data type
print(type(a))  # This is going to show that a is of type "class int"

# lets change data type of a
a = 30.1
print(type(a))  # This is going to give type as floating point.

# Lets change the it to type list
a = ['value1', 'value2']
print(type(a))  # This will show that a is of list type.

# Make sure you do not use built in keywords of python as a variable names
# for example :
# int = 2  # This will throw an error as int is a built in keyword
# list = 30 # same is the case here as well list is built in keyword.

# another example of python variable and building logic using them
my_income = 100
my_rate = 0.1
my_taxes = my_income * my_rate
print(my_taxes)  # So this will compute how much tax do i need to pay

# Strings
# =======
# 1) Sequence of characters, wrapped up in wither single quotes or double quotes
# 2) example
'hello'
"hello"
"I'am Saga"  # Note that here we have to mandatory use the double quotes because we are already using single quotes
# inside the string.
# 3) Strings are ordered sequences so we can apply indexing and slicing on strings.
# 4) Indexing allows to to grab a single character from a string also
# 5) Character :        h  e  l  l  o
# 6) indexing  :        0  1  2  3  4
# 7) reverse indexing : 0 -4 -3 -2 -1
# 8) slicing allows to grab a sub section of a string ==> [start:stop:step]
# 9) start : numerical value for slice start
# 10) stop : index value you will go upto but not include it
# 11) step : size of jump you take

# example of strings
'Hello'
"World"
"This is also a string"  # note that in this statement whitespaces are counted as characters
" I'am a string "  # Notice here it is mandatory that we uses double quotes to avoid confusing python

# 12) To print strings we can make use of print function
print("Hello")
print('Hello')
print("I'am string")

# 13) Escape characters : \n, \t,
print('Hello \nWorld')  # \n new line
print('Hello \tWorld')  # \t tab

# 14) length function is used to calculate the length of the string
print(len('Hello'))
print(len("i am"))  # Notice that here we have character count of 4 which means whitespaces are included as character.

# Indexing and Slicing of String
# ==============================
# Lets have a string variable mystring and lets assigned one string to it")
mystring = "Hello World"
print(mystring)

# Indexing
# =========
print(mystring[0])  # Notice that here we are trying to fetch one letter out of string "mystring" and printing that
# Also notice that indexing in string starts from 0 and spaces are counted as character.

# So to print 'o' of word 'world' in above string we will write
print(mystring[7])
# other examples
print(mystring[-1])  # Remember that -1 index represent last index location. this is also called as reverse indexing
print(mystring[-2])
print(mystring[-3])
# Note that reverse indexing is used to grab the last letter of any big string, without calculating its length,if we
# don;t know how big that string is.
# So lets say
bigstring = "asdfgghhkkdoooeijshdjdkdkfkfsdfs dfhbsdfjsdfsdfjksndfjksndfbsdhfbiuwefufbushdfusdbfhsdfs"
# Now we don't have idea of how long this string is so one way is to calculate the length of the string and then print
# last character of the string. like below
print(bigstring[len(bigstring) - 1])
# instead of above tedious code we could just use reverse indexing as below
print(bigstring[-1])

# Slicing
# =======
# So here we are grabbing sub section of a string
# Let say we want to grab a sub string starting from 2nd letter in the below string and all the way till end
mystring = "abcdefghijk"
# notice that we are redefining the variable mystring in above statement.
print(mystring[2])  # So this is going to give us second element of the string
print(mystring[2:])  # Now this is going to give us a sub string of starting from second character all the way till end
print(mystring[:3])  # Notice here we are grabing string from starting letter, upto(but not including) 3rd letter
# Now suppose we want to grab a subsection of a string from middle. let say "def"
print(mystring[3:6])
# Now lets consider the third parameter of slice that is the step size
# Suppose we want to go grab the dtring from beginning and all the way till end. now there are two ways of doing this
print(mystring)  # So this ultimately going to grab everything from start till end.
print(mystring[::])  # So this notation is technically doing to same thing as above, where it says that starting from
# beginning and going till end.
# lets include third parameter of this that is step size
print(mystring[::2])  # So this is going to grab the complete string from start till end but in a step of 2
# similarly we can also increase the step size
print(mystring[::3])
# Note that we can also use this step size for reversing the string
print(mystring[::-1])  # So this is going to basically going to grab the string from the very start till end but in
# step size of -1, which is logically going to backward by one and hence this is going to reverse the string.

# String properties and Methods
# =============================

# Immutability of a string
# This means that once a string variable assigned a value. Then you cannot change the value of that. because string are
# immutable.
# Lets consider the example:
name = "Sam"
print(name)
# Now suppose we want to change the first letter of name from S to P.
print(name[0])  # This is going to print S, and suppose if we try to reassign the value of name[0] tp P
# name[0] = "p"  # This will throw ans error. as item assignment is not possibe in case of string.
print(name)
# We can do this task with below steps
substr = "P"
print(substr)
name = substr + name[1:]  # So here we have taken help of string concatenation
print(name)
# Another example of string concatenation
x = "Hello World"
print(x + " It is beautiful")
# Notice that in above print statement we have given a space after double quotes before starting the sentence. This is
# because space in python is counted as a character.
# Lets reassign this new concatenated string back to x
x = x + " It is beautiful"
print(x)

# We can also do multiplication of string as well using "*" sign as below
letter = 'z'
print(letter * 10)  # This is going to print z 10 times
# print(letter * 'x') # This is going to throw an error because we can't multiply sequence by non-int of type string.
# Notice that if we try to use + sign between two numbers its going to add the two numbers
y = 3 + 5
print(y)
# but if you try to use + sign between to string character they are going to be concatenated
z = '3' + '5'
print(z)  # This going to give output as 35 and not as 8
# So be careful while using the variables in python as it is very flexible and it may cause an issue later in the code.

# String methods
# ==============

x = "Hello World"
print(x.upper())  # Notice that this upper() function is going to print the uppercase of the string but it is not going
# To change the actual value of string. Hence we can say that upper() is inplace method

print(x.lower())  # To convert string to lower case.

# Now consider another method named as split()
print(x.split())  # So this split() function is going to split the string and create a list with the words in it, based
# on the white space or the letter you are going to pass to this method
print(x.split('l'))

x = "This is a string example"
print(x.split('i'))

# Print formatting with Strings
# ==============================
# Here we are going to study the ways of injecting the variables in the string to print them along with string.
# This is basically called as String Interpolation
# One way of doing this is as below
name_var = "sagar"
print("My name is : " + name_var)
# other two ways
# .format() method
# f-strings (formatted string literals)

# .format() method
# ================
# syntax : 'String here {} then also {}'.format('something1','something2')
# examples:
print("This is a string {}".format("INSERTED"))
print('The {} {} {}'.format('RED', 'GREEN', 'BLUE'))
# Notice in above example colors are inserted in a same order in which they occur inside .format method
# index positions inside the .format method starts from 0 and goes on like 0,1,2,...
print('The {2} {1} {0}'.format('RED', 'GREEN', 'BLUE'))
# This will print "The BLUE GREEN RED"
print('The {0} {0} {0}'.format('RED', 'GREEN', 'BLUE'))
# This will print : "The RED RED RED"
# We can even use the key value pair over as below
print('The {q} {b} {f}'.format(f='Fox', b='Brown', q='Quick'))
# So here we are doing kind of item assignment inside the .format method

# float formatting with the .format() method
# ==========================================
# syntax inside the curly braces will look like this : "{value:width.precision f}"
result = 100/777
print(result)
# o/p : 0.1287001287001287
print('The value is : {r}'.format(r=result))
# o/p: The value is : 0.1287001287001287
print('The value is : {r:1.3f}'.format(r=result))
# o/p: The value is : 0.129
# so the width here is 1 so before decimal only 1 space is taken and after decimal precision is kept upto 3 decimal
# hence rounded upto 3 decimal places.
# Notice that Width on the left side does not means the number of digits, it means number of white spaces
# example
result1 = 104.2345
print('The value is : {r:1.3f}'.format(r=result1))
# o/p: The value is : 104.234

# f Strings (formatted literals)
# ===============================
name = "Sagar"
print(f"The name is : {name}")
# With this way we can directly insert the variable inside the print statement and just put f in front of the string
age = 28
print(f"{name} is {age} years old")
# o/p: Sagar is 28 years old



