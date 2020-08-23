# Tuples are similar to lists.
# The only difference between list and tuple is that tuples are immutable.
# They are represented as (1, 2, 3)

t = (1, 2, 3)
mylist = [1, 2, 3]
print(type(t))
# <class 'tuple'>
print(type(mylist))
# <class 'list'>

print(t)
# (1, 2, 3)
# Just like a list tuple can hold data of different data types
t = ('ONE', 2, 3.4)
print(t)
# ('ONE', 2, 3.4)
# Also since tuples are ordered, hence we can apply indexing and slicing as well to the tuples
print(t[0])
# ONE
print(t[-1])
# 3.4
print(t[1:])
# (2, 3.4)

# methods of tuples
# ==================
# there are total two functions :
# count()
t = ('a', 'a', 'b')
print(t.count('a'))
# 2
print(t.count('b'))
# 1

# index()
# =======
print(t.index('a'))
# 0 , this shows that index method returns the location of first occurance of an element if it appears more than one
# time in a tuple
print(t.index('b'))
# 2

# tuples are immutable
print(t)
('a', 'a', 'b')
# t[0] = 'NEW'
# print(t)
# TypeError: 'tuple' object does not support item assignment
# So item assignment is not allowed in case of tuple.