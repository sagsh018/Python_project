# Sets are unordered collections of unique elements. so that means there can be only one representative of same object
# So lets define a set as below
my_set = set()
print(my_set)
# set()
# So ths shows the empty set as of now
# lets add elements to this set
my_set.add(4)
print(my_set)
# {4}
print(my_set.add(5))
# Notice this print as None type object returned as add() method here is not returning anything and its a inplace method
my_set.add(5)
print(my_set)
# {4, 5}
# Now lets try to add 5 one more time to this set and check whether set accepts that or not
my_set.add(5)
print(my_set)
# {4, 5}
# So the output still remain the same. The reason is that set does not accept duplicate values.

# One of the way sets can be used in is,lets say we have a list as:
my_list = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
# If we cast this list as a set
print(set(my_list))
# {1, 2, 3}
# so we got unique values.

# Also note that since sets are unordered collection of unique elements and can have data of different data types.
# indexing and slicing also not possible in sets.
