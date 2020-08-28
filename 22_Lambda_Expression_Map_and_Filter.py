# So here we are going to study lambda function, but for that we fist need to understand what is map and filer fucntion
# map
# ===

# consider the function, that returns the square of a number
def square(num):
    return num ** 2


# So lets call it
print(square(num=2))
# 4
# but suppose i want to square every number of a list
my_list = [1, 2, 3, 4, 5, 6]
# So one is for loop to square every number of this list
for item in my_list:
    print(square(item))
# 4
# 1
# 4
# 9
# 16
# 25
# 36

# another method to do this is using a map function which takes in two arguments, one is the function that needs to
# be applied and other is the object on which we have to iterate

for item in map(square, my_list):
    print(item)

# 1
# 4
# 9
# 16
# 25
# 36

# so what map function does is, it has taken function square and applied it to every element of a list my_list
# and we have looped onto every element of that result and printed it using a loop

# notice that we haven't got the actual list in the output, to get the actual list we could as below

print(list(map(square, my_list)))


# [1, 4, 9, 16, 25, 36]

# lets consider another example
# suppose we have a list of names and we want to iterate through this list and check if the length of any name is even
# and if it is even just return true and if ots odd, then return first letter of that name,

# So lets write the function first:

def len_even(name):
    if len(name) % 2 == 0:
        return 'EVEN'
    else:
        return name[0]


my_list = ['sagar', 'Andy', 'Rahul', 'greg']
my_list = list(map(len_even, my_list))
print(my_list)


# ['s', 'EVEN', 'R', 'EVEN']

# Now notice that while passing function argument to the map function we are not using parenthesis, because we are
# just providing the function name and map is going to execute it later on every element of the iterable object passed
# as a second argument

# filter
# =======
# So this also works in a same manner, except that, instead of applying the specified function on every item of
# iterable object, filter function helps in filtering out the elements based on the function provided as an argument

# lets consider the function that returns True only if the number is even

def check_even(num):
    return num % 2 == 0


# and suppose we have a list
my_list = [1, 2, 3, 4, 5, 6, 7]
# suppose we want to filer out only the numbers which are even. So we will make use of filter function here.

my_list = list(filter(check_even, my_list))
print(my_list)


# [2, 4, 6]

# So now we know what is map function and filter function.
# We will move on to the lambda function now, by converting a normal function into a lambda expression
# normal function
def square(num):
    result = num ** 2
    return result


print(square(3))


# 9
# Now slowly lets convert this normal function into a lambda function
# firstly we don't need this extra varable named as result in above function. So lets get rid of it

def square(num):
    return num ** 2


print(square(4))


# 16

# Similarly instead of writing the code on multiple line we could write it on a same line

def square(num): return num ** 2


# Now we almost got the form of lambda expression here. the only thing to notice here is that, lambda expressions
# are anonymous and usually the tasks which are required for one time and then you won't refer to in the future
# so in above function you won't even need the function name and replace it with lambda and we don;t even need the
# return while using lambda

lambda num: num ** 2

# So this is it, this is our lambda expression returnung the square of a number, lets store it somewhere
sq_num = lambda num: num ** 2
print(sq_num(2))
# 4

# Now this lambda expression could be used inside the map and filter functions in order to become the first argument
# for these function.
# So instead of defining the separate function like we did for squaring up the numbers inside the list we have defined
# separate function and used it inside the map function.
# what we could do is to use that lambda expression inside the map function and directly get the functionality of the
# function inside it
# lets see the example below

# Suppose we have to write the function again to return the square of every number of a list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(map(lambda num: num ** 2, my_list)))
# [1, 4, 9, 16, 25, 36, 49, 64, 81]
# So we can see, we have easily applied the lambda expression onto this map function.

# Now lets try to use this lambda expression with the filter function

print(list(filter(lambda num: num%2 == 0, my_list)))
# [2, 4, 6, 8]
# so i got my list filtered with the help of filter function which has lambda expression working inside it

# Lets consider another example. Suppose we want to grab the first character of every string inside a list
# lets consider the below script

names_script = ['andy', 'ramesh', 'suresh', 'krishna']

print(list(map(lambda name: name[0], names_script)))
# ['a', 'r', 's', 'k']

# Now suppose i want to reverse every name inside the above mentioned name list

print(list(map(lambda name: name[::-1], names_script)))
# ['ydna', 'hsemar', 'hserus', 'anhsirk']



