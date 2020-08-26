# List comprehensions are unique way of quickly creating list in python
# if you find yourself creating the list with for loop and append(). list comprehensions are better choice
my_list = []
print(my_list)
# [], so we have an empty list
for item in range(1, 10):
    my_list.append(item)
print(my_list)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# another example with this method
my_list = []
for letter in 'hello':
    my_list.append(letter)
print(f'created list is : {my_list}')
# created list is : ['h', 'e', 'l', 'l', 'o']
# So the better way of doing this is with the help of list comprehensions
my_string = 'something'
my_list = [letter for letter in my_string]
print(my_list)
# ['s', 'o', 'm', 'e', 't', 'h', 'i', 'n', 'g']
# So here we have basically flattened down our for loop.
# another example
my_list = [x for x in 'word']
print(my_list)
# ['w', 'o', 'r', 'd']

my_word = input('Enter the word you want list to be created for : ')
print(f'The list created for the word you entered : {[x for x in my_word]}')
# Enter the word you want list to be created for : sagar
# The list created for the word you entered : ['s', 'a', 'g', 'a', 'r']

# Also lets try to flatten the for loop for our first example
my_list = []
print(my_list)
# [], so we have an empty list
for item in range(1, 10):
    my_list.append(item)
print(my_list)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

my_list = [num for num in range(1, 10)]
print(my_list)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# we can even perform operations in this method
# to print double of numbers in range from 1 to 10
my_list = [num*2 for num in range(1, 10)]
print(my_list)
# [2, 4, 6, 8, 10, 12, 14, 16, 18]
# To print square of numbers in range from 1 to 10
print([num**2 for num in range(1, 10)])
# [1, 4, 9, 16, 25, 36, 49, 64, 81]
# To print only even numbers from range 1 to 10
print([num for num in range(1, 10) if num%2 == 0])
# [2, 4, 6, 8]
# To print square of even numbers
print([num**2 for num in range(1, 10) if num%2 == 0])
# [4, 16, 36, 64]

# Suppose we have temperature in Celsius and we want to convert it into Fahrenheit
Celsius = [0, 10, 20, 30, 40]
fahrenheit = [((9/5)*temp + 32) for temp in Celsius]
print(fahrenheit)
# [32.0, 50.0, 68.0, 86.0, 104.0]

# we can not only do if statements in list comprehensions but we can also do the if and ele both
# but this change the order of statement a little bit
my_list = [x if x%2 == 0 else 'Odd' for x in range(1, 10)]
print(my_list)

my_list = []
# Now lets consider the example of nested loops
for x in [1, 2, 3]:
    for y in [10, 100, 1000]:
        my_list.append(x*y)
print(my_list)
# [10, 100, 1000, 20, 200, 2000, 30, 300, 3000]
# Lets try to do this with list comprehension
my_list = [x*y for x in [1, 2, 3] for y in [10, 100, 1000]]
print(my_list)
[10, 100, 1000, 20, 200, 2000, 30, 300, 3000]





