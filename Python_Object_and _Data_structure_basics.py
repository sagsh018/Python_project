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


