# So here we are going to study two functional arguments used a lot. those are :
# *args and **kwargs

# *args
# =====
def my_func(*args):
    print(args)


my_func(20, 30, 40, 50, 60)


# (20, 30, 40, 50, 60)
# So basically *args create a tuple of as many arguments passed at the time of function calling and can be useful
# in case of functions which takes up the tuple and perform the operation
# see the example below

def my_func(*args):
    return sum(args)


print(my_func(10, 20, 30, 40))


# 100


# So since *args create the tuple, so we can apply all the operations of tuple in this
def my_func(*args):
    for item in args:
        print(item)


my_func(10, 20, 30, 40, 50, 60)


# 10
# 20
# 30
# 40
# 50
# 60

# **kwargs - stands for key word arguments
# ========================================
# So **kwargs is a special type of argument that creates dictionary from the given data.
# Example
def my_func(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('The fruit of choice is : {}'.format(kwargs['fruit']))
    elif 'veggie' in kwargs:
        print('The vegetable of choice is : {}'.format(kwargs['veggie']))
    else:
        print('Did not find any fruit or vegetable here in the given data')


my_func(fruit='apple', veggie='lettuce')


# {'fruit': 'apple', 'veggie': 'lettuce'}
# The fruit of choice is : apple
# so here as we have seen that the data we have given to the my_func parameter is taken by **kwargs and converted
# into the dictionary.

# Now lets try to use both the **args and **kwargs in combination

def my_func(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like to have {} {}'.format(args[0], kwargs['food']))


my_func(1, 2, 3, 4, 5, veggie='lettuce', food='eggs')


# (1, 2, 3, 4, 5)
# {'veggie': 'lettuce', 'food': 'eggs'}
# I would like to have 1 eggs

# Notice that here we have used the combination of both args and kwargs, so we have to pass the parameters in a same
# order like we have given as an arguments while defining the function.
# So in short we cannot do any such thing
# my_func(1, 2, 3, 4, 5, fruit = 'orange', food = 'eggs', 6)
# error : SyntaxError: positional argument follows keyword argument

# problem
# ========
# Define a function, that takes arbitrary number of arguments, and returns a list containing only those arguments
# that are even

def even_check(*args):
    my_list = []
    for num in args:
        if num % 2 == 0:
            my_list.append(num)
        else:
            pass
    return my_list


print(even_check(1, 2, 3, 4, 5, 6))


# [2, 4, 6]

# we could also do the same thing with the help of list comprehension

def even_check_another(*args):
    my_list = []
    my_list = [num for num in args if num % 2 == 0]
    return my_list


print(even_check_another(1, 2, 3, 4, 5))


# [2, 4]

# problem
# ========
# Define a function, that takes a string, and return a matching string where every even letter is uppercase and every
# odd letter is lowercase

def my_func(str):
    my_str = ''
    index = 0
    for x in str:
        if index % 2 == 0:
            my_str += x.upper()
        else:
            my_str += x.lower()
        index += 1
    return my_str


print(my_func('sagar'))


