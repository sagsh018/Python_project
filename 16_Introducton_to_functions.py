# So functions are blocks of code containing the repetitive tasks, to use them over and over again
# def keyword
# ============
# def stands for definition of function and it tells python what we are about to write is a function.
# syntax
# ===================================================================================================================
#   def name_of_function(): notice that by default function uses snake casing for function name(means small letters)
#       '''
#       Docstring explains functions
#       '''
#       print('Hello')
# ==================================================================================================================
# to run this function
#   name_of_function()
# o/p: Hello

# Now consider below case where we are passing arguement to the function to work within block of its code
# ==================================================
#   def name_of_function(name):
#       '''
#       Docstring explains functions
#       '''
#       print('Hello' + name)
# ==================================================
# To call this
#   name_of_function('sagar')
# o/p: Hello  sagar

# we can also use return keyword inside function and return keyword is used to return the value of function which
# can be saved into the variable and thats make difference between print which just print output to console. whereas
# return gives back the value which could be stored in some variable and can be used later.
# example
def add_function(num1, num2):
    return num1 + num2


# So this function is returning a value which we can store let say in a variable 'result'
result = add_function(1, 2)
print(result)


# 3

#  Now lets create a function
def say_hello():
    print('Hello')
    print('how')
    print('are')
    print('you')


# Now lets call this function
say_hello()
# Hello
# how
# are
# you
# Here we have seen that there are 4 print lines in the above function but we have to call the function just one time
# to print all 4 lines
# Also notice if you call the function without ()
say_hello


# This will not give any output and notice that we have to use () when we are calling any function

# Now lets override our function to function with arguments
def say_hello(name):
    print(f'Hello {name}')


say_hello('sagar')


# Hello sagar
# we can give some default value as well for an argument while defining the function so that in case if you forget
# to pas in the parameter while calling the function, it won't give any error
# for example, if i call above function without parameters, then it will throw an error
# say_hello()
# TypeError: say_hello() missing 1 required positional argument: 'name'
# So to overcome this mistake we can pass in the default parameter to the function definition
def say_hello(name='default'):
    print(f'Hello {name}')


say_hello('Sagar')
# Hello Sagar
say_hello()


# Hello default
# So when we forgot to pass the parameter while calling the function, it took the default value and gave the output
# but didn't ran into error

# Now lets understand the use of return statement in method
# with return statements inside function, we can actually get the chance to store the value returned by function into
# the variable and use later into the course.

def return_result(num1, num2):
    return num1 + num2


result = return_result(20, 30)
print(result)


# 50


# Notice that we can use both print statement and retuen statemets in function together as well
def my_func(a, b):
    print(a + b)
    return a + b


result = my_func(10, 20)
# 30
# Notice that we haven't printed what is there inside result yet, we just called the function and because of
# print statement, it has printed 30
# we can letter print same result with the help of result as well
print(result)


# 30

# important note.
# =================
# Since python is dynamically typed language, so while defining the function we are no where mentioning that what
# type of data need to be passed as a parameter while calling it.
# So suppose we have below function which adds two numbers
def add_func(a, b):
    print(a + b)


add_func(10, 20)
# 30
# but suppose if someone pass in the string instead of numbers then what will happen
add_func('10', '20')
# 1020
# So the result has changed completely. So since we have this leverage in python to not define any data type before
# using it, but this creates the problems and bugs
# for now keep this in mind, we will tackle this problem letter 
