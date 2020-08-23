# Dictionaries are unordered, key-value paired based.
# No indexing and slicing for this as unordered
# We can quickly grab the element in dictionary with knowing the index location with the help of key

# Syntax : {'key1':'value1', 'key2':'value2'}
# Also note that Dictionaries cannot be sorted as they are not ordered.
# So we should choose dictionaries when we wnat to quickly retrieve the element without knowing the index location of
# the element.

my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict)
# {'key1': 'value1', 'key2': 'value2'}

# To get the value for a key
print(my_dict['key1'])
# value1
print(my_dict['key2'])
# value2

# Use case of dictionary is :
prices_lookup = {'apple': 20, 'Orange': 30, 'Milk': 50}
print(prices_lookup['apple'])
# 20
# So we can  easily see the price of a apple without knowing the exact location of the apple in the dictionary

# Another point to note here is that dictionaries can hold data of different data types and even they can hold the
# entire lists also. as well as you can have dictionary as a element of a dictionary also.
d = {'k1': 123, 'k2': [0, 1, 2, 3], 'k3': {'inside_key': 100}}
print(d)
# {'k1': 123, 'k2': [0, 1, 2, 3], 'k3': {'inside_key': 100}}
print(d['k1'])
# 123
print(d['k2'][1])
# 1, So we can see that using multiple key and index value we have choose the value '1'
print(d['k3']['inside_key'])
# 100, So here we have used multiple keys  and grabbed 100
# Lets take another example
d = {'k1': ['a', 'b', 'c']}
print(d)
# {'k1': ['a', 'b', 'c']}
# To grab the list
print(d['k1'])
# ['a', 'b', 'c']
# To grab the third element of string
print(d['k1'][2])
# c
# Suppose we also want capitalize the C
print(d['k1'][2].upper())
# C

# To add a new key:value pair to the already existing Dictionary
d = {'k1': 100, 'k2': 200}
print(d)
# {'k1': 100, 'k2': 200}
# lets add new key and value pair
d['k3'] = 300 # This will simply add the k3 key along with the value to the end of the dictionary
print(d)
# {'k1': 100, 'k2': 200, 'k3': 300}

# Notice that Dictionaries are also mutable, So we can change the value corresponding to the key by using below
# method
print(d)
# {'k1': 100, 'k2': 200, 'k3': 300}
d['k1'] = 'NEW_VALUE'
print(d)
# {'k1': 'NEW_VALUE', 'k2': 200, 'k3': 300}

# Also we can use methods for dictionaries in order to get all the keys, or all the values and also both the
# key and value
d = {'k1': 100, 'k2': 200, 'k3': 300}
print(d)
# {'k1': 100, 'k2': 200, 'k3': 300}
print(d.keys())
# dict_keys(['k1', 'k2', 'k3'])
print(d.values())
# dict_values([100, 200, 300])
print(d.items())
# dict_items([('k1', 100), ('k2', 200), ('k3', 300)])
# note that in above output the pairs ('k1', 100), ('k2', 200), ('k3', 300) are nothing but the tuples.
