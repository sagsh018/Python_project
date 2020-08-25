# We can apply for loop in order to iterate over anything that is iterable.
# Syntax of for loop
#   my_iterable = [1,2,3]
#   for item_name in my_iterable:
#       print(item_name)
# o/p:
# 1
# 2
# 3

# example
# =======

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in my_list:
    print(num)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in my_list:
    print('Hello!')
# Hello!
# Hello!
# Hello!
# Hello!
# Hello!
# Hello!
# Hello!
# Hello!
# Hello!
# Hello!

for num in my_list:
    if num % 2 == 0:
        print(f'Even number : {num}')
    else:
        print(f'Odd number : {num}')
# Even number : 0
# Odd number : 1
# Even number : 2
# Odd number : 3
# Even number : 4
# Odd number : 5
# Even number : 6
# Odd number : 7
# Even number : 8
# Odd number : 9

list_sum = 0
for num in my_list:
    list_sum += num
print(list_sum)
# 45

list_sum = 0
for num in my_list:
    list_sum += num
    print(list_sum)
# 0
# 1
# 3
# 6
# 10
# 15
# 21
# 28
# 36
# 45
# So we can see that as we have indented the print statement, it came inside for loop and ran for every iteration

for letter in 'Hello World!':
    print(letter)
# H
# e
# l
# l
# o
#
# W
# o
# r
# l
# d
# !

for letter in 'Hello World!':
    print('cool')
# So this will just print cool for number of letters in above string of 'Hello World!'
# instead of using a variable like 'letter' here we can just give a _ simply
for _ in 'Hello World':
    print('cool')
# Since we do not need a variable to iterate as we just have to print cool. so we have just used _

# lets apply for loop to tuple
tup = (1, 2, 3)

for item in tup:
    print(item)
# 1
# 2
# 3

# lets consider below list containing the tuples itself
my_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(my_list)
# [(1, 2), (3, 4), (5, 6), (7, 8)]
print(len(my_list))
# 4, so every tuple inside this list is considered as a item
# now lets apply for loop to this list
for item in my_list:
    print(item)
# (1, 2)
# (3, 4)
# (5, 6)
# (7, 8)
# So here we got the tuple as the items inside the list.

# Now suppose if we iterate over this list with the variable of a form of item inside list(tuple in this case) then
# we can get the individual elements of this data structure (tuple) and that would be called as tuple unpacking
# lets consider the example

for (a, b) in my_list:
    print(a)
    print(b)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# So this is how we have unpacked the tuple
# we can even capture just the one element of tuples
for (a, b) in my_list:
    print(a)
# 1
# 3
# 5
# 7
# Also there is no need to put the variable we are using inside braces
for a, b in my_list:
    print(a)
# 1
# 3
# 5
# 7

# Lets consider another example
my_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for item in my_list:
    print(item)
# (1, 2, 3)
# (4, 5, 6)
# (7, 8, 9)
# So now do the tuple unpacking
for a, b, c in my_list:
    print(b)
# 2
# 5
# 8

# Now lets try to iterate in dictionary using for loop
my_dict = {'k1': 1, 'k2': 2, 'k3': 3}
for item in my_dict.items():
    print(item)
# ('k1', 1)
# ('k2', 2)
# ('k3', 3)
# Notice that while iterating instead of just mentioning the name of the dictionary we have to mention .item()
# in order to have complete elements of dictionary
# Now we can clearly see that for loop returned the items of dictionary as a tuples
# so we can apply tuple unpacking here as well
for k, v in my_dict.items():
    print(k)
# k1
# k2
# k3
# So only got keys
# to get the value lets do this
for k, v in my_dict.items():
    print(v)
# 1
# 2
# 3

# Also we can get back the keys and values with below method as well
for item in my_dict.keys():
    print(item)
# k1
# k2
# k3
for item in my_dict.values():
    print(item)
# 1
# 2
# 3
# Notice that dictionaries are unordered hence its not neccessary that you always get the out in a sequence you put
# inside the dictionary.

