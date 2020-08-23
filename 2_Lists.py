# Kind of array in python. but only difference is they can hold data of different data types

my_list = [1, 2, 3]
# This is simple example of a list
print(my_list)
# o/p: [1, 2, 3]

my_list = ['STRING', 100, 300.5]
# So this is a list of different data types.
print(my_list)
# o/p: ['STRING', 100, 300.5]

# To calculate the length of the string
print(len(my_list))

# Lists are ordered sequences hence indexing and slicing is applicable on lists
my_list = ['one', 'two', 'three']
print(my_list[0])
# o/p: one
print(my_list[0:])
# o/p: ['one', 'two', 'three']
print(my_list[1:])
# ['two', 'three']

# concatination of lists
another_list = ['four', 'five']
Total_list = my_list + another_list
print(Total_list)
# ['one', 'two', 'three', 'four', 'five']

# So all these operations which we did above are similar to the ones we did with string, the only difference here
# is that lists are mutable. So we can change the value of a list element

another_list[0] = 'six'
print(another_list)
# ['six', 'five']
# So we have changed the 'four' with 'six'
# lets try it one more time
Total_list[0] = 'ONE ALL CAPS'
print(Total_list)
# ['ONE ALL CAPS', 'two', 'three', 'four', 'five']

# appending new element at the end of a list
Total_list.append('six')
print(Total_list)
# ['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six']
Total_list.append('Seven')
print(Total_list)
# ['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six', 'Seven']
# notice that this append() method is a inplace method and its changing the value of a list in place.

# Removing the last element from the list : pop() method
Total_list.pop()
print(Total_list)
# ['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six']
# Notice that pop() method pop out the last method and also returned it. So if we try to store it in other variable
# we can do so
popped_ele = Total_list.pop()
print(popped_ele)
# six
# To remove the element at a specified index location we can pass the element location in the pop() method
popped_ele2 = Total_list.pop(0)
print(popped_ele2)
print(Total_list)
# ONE ALL CAPS
# ['two', 'three', 'four', 'five']
# Notice that default value in the pop() mehtod is "-1" as it is always popping out the last element by default

# So we can also use the reverse indexing in lists

# sort method on list
# ===================
my_list = ['a', 'x', 'd', 'c', 'e']
num_list = [3, 2, 6, 4, 7]
# So these two are unsorted list, if we want to sort them we can use the sort method
my_list.sort()
print(my_list)
# ['a', 'c', 'd', 'e', 'x']
# So the sort() method is also a unplace method
# Also notice that sort method does not return anything
# it return None type object which is just a place holder in python
print(num_list.sort())
# None
# So we can see that we tried to print the value returned by the sort method, but it has returned None as this is
# inplace method and does not return anything.
# similarly we can sort the num list also
num_list.sort()
print(num_list)
# [2, 3, 4, 6, 7]

# Reverse method for lists
# =========================
print(my_list)
# ['a', 'c', 'd', 'e', 'x']
my_list.reverse()
print(my_list)
# ['x', 'e', 'd', 'c', 'a']
# Notice that reverse() method is also inplace method and does not return anything

