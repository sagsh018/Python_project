# So here we are going to take a look at the object oriented programming and its concepts.
# OOPs allows programmers to create their own objects that have methods and attributes
# Then with the help of these object we create using OOPs, we can call the methods and use there attributes in our
# program.

# Notice below,

my_list = [1, 2, 3, 4, 5]
# So here we have created a list my_list, so by default my_list will act as a object of type list and with the help
# of my_list we can call the methods of list which are already predefined inside python like below

my_list.append(6)
print(my_list)


# [1, 2, 3, 4, 5, 6]
# So this is how we have used one of the inbuilt method of class list, via its object "my_list"
# notice these methods act as a functions that use information about the object, as well as the object itself to return
# the result or change the current object. like we have changed the list in above example

# So OOPs allows users to create there own objects which they can use to access the methods and attributes of the
# objects or the object itself.

# Now lets have a look at the syntax of defining the class/objects inside a python which will contain the methods and
# attributes and later we can create instance of that class/object to access the methods and attributes of that class

# class NameOfClass():
#   def __init__(self, param1, param2):
#       self.param1 = param1
#       self.param2 = param2
#
#   def some_method(self):
#       print(self.param1)

# Notice that class name follows Camel casing, i.e. first letter of every word making up the class name is capital.
# whereas variable names and function names follow the snake casing, i.e small letters with underscores in between

# Now lets go ahead and create our first class/object


class Sample():
    pass


# So this is just a class defined and this class does not have anything defined inside it, it is just acting as a
# place holder as of now.
# Now lets try to create an object for this class

my_sample = Sample()
print(type(my_sample))


# <class '__main__.Sample'>
# So this is how we have created a instance of object/class Sample.

# Now lets create another class named as Dog and try to define a attribute for that class

class Dog():
    def __init__(self, breed):
        self.breed = breed


# notice that __init__ can be considered as a constructor of this class and its going to be called automatically,
# as soon as you create instance of this class.

# So now we have defined a class and added one attribute to that named as breed. notice that self.breed, is a way
# of referring to the attribute value inside the object and that is assigned a value from the global variable breed.

# now lets create a instance for this class

my_dog = Dog('Lab')
# so my_dog is a instance name and we are passing parameter 'Lab' which will become the global variable, and this
# value will be assigned to the local breed variable in the class.

# now lets try to use the attribute of class Dog with the help of instance my_dog

print(my_dog.breed)


# now lets override the dog class having more variables

class Dog_new():

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name

        # spots here need boolean value to be passed in, This is one of the shortcoming of python being so
        # flexible, as we have to provide this documentation along with the code here.
        # otherwise the person using your code will not be sure of the type of data spots is holding and he can pass
        # in the string or any other data type
        self.spots = spots


my_dog = Dog_new('Huskie', 'Tucker', False)
print(my_dog.name)
# Tucker
print(my_dog.breed)
# Huskie
print(my_dog.spots)


# False.

# So till now we have seen the attributes defined for particular species of a dog, but there may be attributes that
# would be same for the entire Dog class. for example species of a dog is mammal and is same for all the dogs
# So such type of attributes are defined at a class object level, above the init method inside the class definition
# Also since these attributes are same for all the dogs we don't use self to refer them.

# So lets consider the example of these

class DogNewAgain():
    # class object attribute
    # Same for any instance of a class
    species = 'mammal'

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name

        # boolean expected for this
        self.spots = spots


my_dog = DogNewAgain('Golden retriever', 'tucker', False)
print(my_dog.species)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)


# mammal
# Golden retriever
# tucker
# False
# so we are able to print the species and its going to be there for all type of dogs, i.e. for all instances of Dog
# class
# notice that we haven't pass species as a parameter while instantiating the object of class Dog, but it is available
# for all instance of dogs

# Now lets study about the methods inside the class.
# So the methods are the functions defined inside the class which are basically the actions and takes up the object
# and its attributes to action upon

# lets consider another class definition with the method included this time

class DogWithMethod():
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def bark(self):
        print('Woof!')


# now lets create instance of this class

my_dog = DogWithMethod('lab', 'Frankie')

print(my_dog.breed)
print(my_dog.name)
my_dog.bark()


# lab
# Frankie
# Woof!
# So our class method has actually performed an action that the actual object did
# now here the method bark is not doing much, and just printing a word. but usually methods do perform some actions
# on the attributes of the objects itself
# for example, let the dog bark its own name

class DogWithMethod():
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def bark(self):
        print('Woof! i am {}'.format(self.name))


my_dog = DogWithMethod('lab', 'Frankie')

print(my_dog.breed)
print(my_dog.name)
# my_dog.bark()


# lab
# Frankie
# Woof! i am Frankie
# notice here with the name in the print statement we are using self keyword just to make sure that we are printing
# name of the dog for that instance, which we have created.

# now we can also pass in the outside argument to the methods of the class, but those are to be provided as the
# parameters while calling them and they are not related to any object hence we don't make use of the self keyword
# while passing them as argument

# consider the example with the outside argument with method of the class

class DogWithMethod():
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def bark(self, number):
        print('Woof! i am {} and the number is {}'.format(self.name, number))


my_dog = DogWithMethod('lab', 'sammy')
# my_dog.bark()
# So notice if you call the method bark of class without passing the parameter, its going to give an error this time
# because its expecting the argument this time from outside of class
# TypeError: bark() missing 1 required positional argument: 'number'
# So we will have to pass in the parameter to call this method of the class this time

my_dog.bark(10)
# lab
# Frankie
# Woof! i am sammy and the number is 10

# Now lets create yet another class named as circle

class Circle():

    # CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius
        self.area = Circle.pi*self.radius*self.radius

    def get_circumference(self):
        return 2*self.radius*Circle.pi

my_circle = Circle(10)

print(my_circle.get_circumference())
# 62.800000000000004

my_circle = Circle(30)
print(my_circle.get_circumference())
# 188.4
# So now this is a second instance which we have created for circle class with the radius as 30 this time

# we can also notice couple of things in the above class definition, that the attribute area is calculated on the
# based on the other attributes and we haven't passed the value for that while creating the instance of class.
# so this is also one way of creating the attribute.

# Also notice that while using the class object attributes like pi in above case we have used it with the reference
# to class name. i.e. "Circle.pi" as it is not specific to the instance of and object, it is same for all the instance
# of an object, so it is object level.






