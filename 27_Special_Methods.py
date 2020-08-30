# Here we are going to study some of the special methods.
# these special methods allows to use some builtin operations in python, such as the length function, the count funtion
# with our own user created objects

# examples

# Suppose we have a list created with name my_list
my_list = [1, 2, 3, 4, 5, 6]
# My_list here is nothing but a kind of an instance for class/object List.
# and if we want to calculate the length og this list we could do with as:
print(len(my_list))


# 6
# Notice that we are able to make use of this builtin function len() function against the instance of List defined above

# Now suppose we have our own object/class

class Sample():
    pass


# So this is simple class, not doing anything, lets create its instance

my_sample = Sample()
# So my_sample is similar to the list instance my_list, So lets try to calculate the length of this instance as well
# print(len(my_sample))
# TypeError: object of type 'Sample' has no len()
# So python complained that you don't any such method with the name of len() inside class Sample so you won;t be able
# to calculate the length of the instance of class Sample()
# similarly if we try to print the instance of class list
print(my_list)
# [1, 2, 3, 4, 5, 6]
# but if we try to print the instance of class Sample
print(my_sample)


# <__main__.Sample object at 0x00000000027B92B0>
# we are getting the memory location of the instance we have created for that object


# So we are going to study the way in this lecture so that we could also make use of the builtin methods and functions
# with our own created class and objects

# we could actually achieve this with the help of special methods

# Suppose we have a class named as Book

class Book():
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


# Now lets create the instance of this class

b = Book('Python rocks', 'sagar', 200)
# now if we try to print the instance b of this class, like we are able to print my_list.
print(my_list)
# [1, 2, 3, 4, 5, 6]
print(b)
# <__main__.Book object at 0x00000000021BE630>
# so in our case when we are trying to print the instance of class we have created, we are not getting the value,
# rather we are getting the memory location of that instance inside the memory on computer
# So whats actually happening here is that, when we use the print function to pring b, print is checking whats the
# string representation of b
# so lets check whats the string representation of b
str(b)


# <__main__.Book object at 0x0000000001DAE630>
# so print is getting this string representation and its printing the same.
# So rather than relying on this type of methodology to print the instance of class we are creating, we can
# include special method called as __str__ in our class definition

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'Title of book is {self.title} and is written by {self.author} and contain {self.pages} pages'


# So now in this class definition, we have mentioned special method so if any of the function asks this class instance
# that whats you string representation. it can give the str representation and return what we have mentioned inside that
# function

# now lets create the instance of this Book class

b = Book('python_rocks', 'Sagar', 200)
print(b)
# Title of book is python_rocks and is written by Sagar and contain 200 pages
# So now with the help of this special method __str__ we are able to make use of inbuilt print() to print instance
# of our class

# similarly if you remember we are unable to calculate the length of our instance like we were doing for my_list
print(len(my_list))


# 6

# len(b)
# TypeError: object of type 'Book' has no len()
# So to handle this we will need another special method named as __len__(self)

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'Title of book is {self.title} and is written by {self.author} and contain {self.pages} pages'

    def __len__(self):
        return self.pages


# So in our example, the length of the book can be checked with the help number of pages it has. so we have returned
# the number of pages for book of that instance.

b = Book('python', 'sagar', 200)
print(len(b))


# 200
# So we are good with this

# Another thing to point out here, if we want to delete the intance or a variable from the python memory
# we could use del for that

# del b
# print(b)
# NameError: name 'b' is not defined
# So the instance we have created of class Book has been deleted and no more exist.
# nut if you notice when we ran del(b) the instance has benn deleted but we did not get any message printed
# like instance deleted. So to add this extra functionality on deletion of an instance of class Book
# lets add another special method
# but for this lets create a different class

class Register():
    def __init__(self, name, color, pages):
        self.name = name
        self.color = color
        self.pages = pages

    def __str__(self):
        return f"This is a {self.name} register, of {self.color} color with {self.pages} pages"

    def __len__(self):
        return self.pages

    def __del__(self):
        print(f'deleted')


reg = Register('rakul', 'green', 500)
print(reg)
# This is a rakul register, of green color with 500 pages
print(len(reg))
# 500
del reg
# deleted
print(reg)
# NameError: name 'reg' is not defined

# So here we have came across 4 special methods
# 1) __init__
# 2) __str__
# 3) __len__
# 4) __del__
