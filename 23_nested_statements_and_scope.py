# In this lecture we are going to discuss the variable scopes inside the nested statements.

# consider the below example, which explain the scope of a variable
x = 25


def printer():
    x = 50
    return x


print(x)
# 25
# So we noticed that we got the result as 25 and not as 50 because we haven't called the printer function we called
# print function and print took x defined outside of function.
print(printer())
# 50
# So we have noticed that when we called printer function inside the print function it has printed x inside the
# printer function and not overridden the value defined outside the printer function

# python follows LEGB Rule in order to work with scope resolution
# L:Local - Names assigned in any way within a function (def or lambda), and not declared global in that function
# E:Enclosing function locals - Names in the local scope of any and all enclosing functions (def or lambda), from
#   inner to outer
# G:Global(module) - names assigned at the top level of a module file, or declared global in a def within the file.
# B:Build-in(python) - Names pre assigned in the built-in names module.

# lets see the examples of all of these one by one

# L:local
# ========
# example : lambda num: num**2

# E:Enclosing function locals
# ============================
# example
name = 'THIS IS A GLOBAL STRING'


def greet():
    name = 'Sammy'

    def hello():
        print('Hello ' + name)

    hello()


greet()
# Hello Sammy
# Now firstly function hello() is going to execute and as soon as it gets the print statement, it will search for name
# variable, now name variable will be checked according to the rule LEGB.
# So first the variable is checked in local scope of function hello(), and we don't have it in hello() function locally.
# next we have to check it in E:Enclosing function local. here we found it defined. so this will be printed.

# Now suppose if comment out the enclosing function local
name = 'THIS IS A GLOBAL STRING'


def greet():
    # name = 'Sammy'

    def hello():
        print('Hello ' + name)

    hello()


greet()
# Hello THIS IS A GLOBAL STRING
# So now firstly L:local will be checked and not found, then E:Enclosing function local checked and not found, then
# Global is checked and found, hence that will be printed.

# consider another example

name = 'GLOBAL'


def scope():
    name = 'ENCLOCAL'

    def hello():
        name = 'LOCAL'
        print(name)

    hello()


scope()
# since we have a local variable, then that will be printed first
# LOCAL

# Consider another example to understand the scope of variables

x = 50


def func(x):
    print(f'value of x is {x}')

    # local reassignment
    x = 200
    print(f'value of x after reassignment is {x}')


func(x)
# value of x is 50
# value of x after reassignment is 200
# Now notice that we have overridden the value of x, but which x, global one? or local one to the func function
# lets check it out

print(x)
# 50, so this again remains 50 only so the local copy of the function func is overridden

# Now suppose you want to override the global variable only and not the local copy of that. in this case, instead
# of passing the x as an argument, we can use global keyword inside the func function as below

x = 'GLOBAL'


def func():
    global x
    print(f'value of x is {x}')

    x = 'REASSIGNED VALUE OF GLOBAL VARIABLE'
    print(f'value of x after reassignment is {x}')


func()
# value of x is GLOBAL
# value of x after reassignment is REASSIGNED VALUE OF GLOBAL VARIABLE

# So as soon as we are entering inside the function, we are telling python to go inside the global namespace and
# take the value of x from there and do all the modification on that

# Now if we print the value of x it will us the value changed at global level

print(x)
# REASSIGNED VALUE OF GLOBAL VARIABLE

# but this global variable is powerful and not always advisible to be used. so for overriding the global variable
# we could do as below instead of above.

x = 'GLOBAL'


def func(x):
    print(f'value of x is {x}')

    x = 'Enclosing function local'
    print(f'value of x after reassignment is : {x}')
    return x

print(x)
# GLOBAL
x = func(x) # So here explicitly we are changing the value of global x variable with the value returned by function
# GLOBAL
# value of x is GLOBAL
# value of x after reassignment is : Eclosing function local
print(x)
# Enclosing function local
# So this is another way and safe of modifying the global variable
