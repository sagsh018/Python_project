# Here we are going to study some of the important functions or operators
# range()
# =======
# syntax : range(start, end, step)
for item in range(10):
    print(item)
# This will print numbers starting from 0 upto but not including 10
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

for item in range(3, 10):
    print(item)
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# so here we have mentioned step size

for item in range(1, 10, 2):
    print(item)
# 1
# 3
# 5
# 7
# 9
# here we have also mentioned step size

# we can also cascade the range function into list and that will generate the list for us
print(list(range(10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Now if you will try to print directly the range function it will not work, as range is a special type of function
# known as generator. so it need something to print the value instead of itself directly

# enumerate()
# ===========
# This is used to enumerate on some sort of iterable object
# lets consider the examples before using enum
index_counter = 0
for letter in 'abcdefgh':
    print('The value at index {} is {}'.format(index_counter, letter))
    index_counter += 1
# The value at index 0 is a
# The value at index 1 is b
# The value at index 2 is c
# The value at index 3 is d
# The value at index 4 is e
# The value at index 5 is f
# The value at index 6 is g
# The value at index 7 is h
# So in order to print the index for all the letter ins a word we have use extra counter which is going to incremented
# for every letter
# another way of doing the same thing is:
index_counter = 0
word = 'abcdefgh'
for letter in word:
    print(word[index_counter])
    index_counter += 1
# a
# b
# c
# d
# e
# f
# g
# h

# So do these guys of common operations( where we want the index location along with the value at that index and get
# rid of this extra counter variable, we have enumerate() function in python

word = 'sammy'
for item in enumerate(word):
    print(item)
# (0, 's')
# (1, 'a')
# (2, 'm')
# (3, 'm')
# (4, 'y')
# So notice that with the help of enumerate function we easily got the letter of a word alsong with its index in a form
# in a form of tuple
# since we are getting tuples with enumerate function we can do the tuple unpacking here
word = 'Sagar'
for index_loc, letter in enumerate(word):
    print(index_loc)
    print(letter)
    print('\n')
# 0
# S
#
#
# 1
# a
#
#
# 2
# g
#
#
# 3
# a
#
#
# 4
# r
# So we got the letter of the word along with there index locations

word = 'Sagar'
for index_loc, letter in enumerate(word):
    print(f'{letter} is at index location {index_loc}')
# S is at index location 0
# a is at index location 1
# g is at index location 2
# a is at index location 3
# r is at index location 4

# you can also get only letters

word = 'example'
for i, l in enumerate(word):
    print(l)
# e
# x
# a
# m
# p
# l
# e

# zip()
# =====
# This is used to zip two or more lists and return the lists in a form of tuples
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [100, 200, 300]
print(zip(list1, list2, list3))
# <zip object at 0x00000000027D3588>, notice that we didn't get the expected result because zip does not return
# anything, its just generator function, over which we can iterate
for item in zip(list1, list2, list3):
    print(item)
# (1, 'a', 100)
# (2, 'b', 200)
# (3, 'c', 300)
# So again we got the tuples, so we can do the tuple unpacking here as well.
# now suppose if we have uneven lists.
list4 = [1, 2, 3, 4, 5, 6]
list5 = ['a', 'b', 'c']
for item in zip(list4, list5):
    print(item)
# (1, 'a')
# (2, 'b')
# (3, 'c')
# So we can notice that zip only zip up the lists upto the shortest list size.
# we can cast them into list
print(list(zip(list1, list2, list3)))
# [(1, 'a', 100), (2, 'b', 200), (3, 'c', 300)]

# in()
# ====
#  This can be used in order tot check whether an element is present inside the list. Also we have already seen the
# use of in operator in for loop
# example
# ========
print('x' in [1, 2, 3])
# False
print(2 in [1, 2, 3])
# True
# in works with strings as well
print('a' in 'a world')
# True
# in works with dictionary as well
print('key1' in {'key1': 100, 'key2': 200, 'key3': 300})
# True
print(200 in {'key1': 100, 'key2': 200, 'key3': 300})
# So even though our value 200 is present in the dictionary, but it will still return False
# False
# to check the values
d = {'k1': 100, 'k2': 200, 'k3': 300}
print(200 in d.values())
# True
print('k1' in d.keys())
# True

# min and max function
# ====================
my_list = [10, 20, 30, 40, 100]
print(f'minimum number in my_list is : {min(my_list)}')
# minimum number in my_list is : 10
print(max(my_list))
# 100

# random library
# ==============
# Here we are going to import the random library and its functions to use them

from random import shuffle
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(shuffle(my_list))
# None
# No we got None because shuffle is a inplace method of random library, which does not return anything.
print(my_list)
# [2, 4, 7, 10, 1, 6, 9, 3, 12, 5, 11, 8]
# So shuffle did scrambled the elements inside the list but have not returned anything

# Lets consider another method 'randint'. This return random integer from the given starting and ending limits
from random import randint
print(randint(0, 100))
# 54

# input()
# =======
# This input function is used to accept input from user. and note that whatever is passed to an input function
# it accept it as a string.
result = input('What is you name : ')
print(f'Entered name is : {result}')
# What is you name : sagar
# Entered name is : sagar

result = input('Enter any number : ')
print(f'Entered number is : {result}')
# Enter any number : 34
# Entered number is : 34
print(type(result))
# <class 'str'>
# So if you noticed that even though we have entered an integer, input function still accepts string.

# so in order to cast that, we can do the type casting
print(type(int(result)))
# <class 'int'>

age = int(input('Enter your age : '))
print(f'Age you have entered is : {age}')
# 28
print(f'Data type of entered age is : {type(int(age))}')
# Data type of entered age is : <class 'int'>



