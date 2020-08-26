# So here we are going to have a look at how we can get what all methods are there for a given object
# for example suppose if we have a list
my_list = [1, 2, 3, 4, 5, 1]
# So we can see what all methods does it have by using "my_list." and then press tab to check the list of methods
# available
my_list.append(2)
print(my_list)
# [1, 2, 3, 4, 5, 1, 2]

# you can also have a look at the documentation for any function by using help inside pycharm
help(my_list.insert)
# Help on built-in function insert:
#
# insert(index, object, /) method of builtins.list instance
#     Insert object before index.
# Notice that while asking for help we have not put braces in front of insert method of list

# another way of getting help from python documentation over web
# https://docs.python.org/3/

