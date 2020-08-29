# In this lecture we are going to focus on inheritance and polymorphism
# Inheritance -- It is a way for forming a new class from the classes which are already been defined
# Advantage of inheritance is the ability to reuse the code that we have already worked on and to reduce the complexity
# of the program

# So lets go ahead and simple class and that will be called as a base class

class Animal():

    def __init__(self):
        print("Animal Created")


# now lets create an instance of this class

my_animal = Animal()


# Animal Created
# now notice that we have just created the instance of this base class animal and automatically the constructor
# inside that class is called and it has printed the statement

# Now lets add two more methods to this class

class Animal():

    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an Animal")

    def eat(self):
        print("I am eating")


# So here we have on __init__ constructor and two methods. lets create an instance for this now

my_animal = Animal()
# Animal Created

my_animal.who_am_i()
# I am an animal

my_animal.eat()


# I am eating

# Now this animal class is going to act as a base class and other new classes can inherit some of the methods of this
# class if they want.

# lets create new class Dog. So Dog is ultimately an animal, so we can use some of the already defined methods in
# animal class in this class.
# so we are going to inherit class Animal inside class Dog and Dog class will be called as derived class

class Dog(Animal):  # Notice we are passing this time the name of the class to be inherited
    def __init__(self):
        Animal.__init__(self)
        print("The animal is Dog..!")


# So in derived class Dog we have inherit the base class Animal and we are also using one of the method of Animal class
# i.e. __init__ and this is a constructor so as soon as this is called inside the derived class, this is going to
# execute and print the statement
# lets create the instance of Dog class now

my_dog = Dog()
# Animal Created
# The animal is Dog..!

# Now notice that we have inherit the base class Animal inside our derived class
# now since we have inherit the base class Animal, we can use the methods of that class with the help of instance of
# derived class without writing them in our derived class, so this is how i am reusing the code witten once
my_dog.eat()
# I am eating
my_dog.who_am_i()


# I am an Animal

# Now we can also override the methods of base class in our derived class by using below

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog is created")

    def who_am_i(self):
        print("I am a Dog")


# So now if we create the object of derived class Dog and try to access the method of base class, let see what do we get
my_dog = Dog()
# Animal Created
# Dog is created
my_dog.who_am_i()
# I am a Dog
# so i am getting the overridden value
# now lets create an instance of Animal class again
my_animal = Animal()
# Animal Created
my_animal.who_am_i()


# I am an Animal
# So original value is printed. So here we have override the method of base class inside derived class
# We can even add on the methods in the derived class

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def who_am_i(self):
        print("I am a Dog")

    def eat(self):
        print("I am eating and i am dog")

    def bark(self):
        print("Woof!")


my_dog = Dog()
# Dog created
my_dog.who_am_i()
# I am a Dog
my_dog.eat()
# I am eating and i am dog
my_dog.bark()


# Woof!
# So now we have seen finally that we can inherit the base class into derived class by just passing the class name
# while defining the class and after that we can use the methods of base class without mentioning them in the drived
# class.
# Also if we like to override them, then we can just define the same method again with the same name and make the
# required changes.
# also from the above example we could see that we can also add on the new methods to the derived class.
# So this is all about the Inheritance in Python.

# lets move on to Polymorphism
# example

class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says WOOF!"


class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says MEOW!"


# Now lets create two instances of Dog and Cat class

niko = Dog('NIKO')
felix = Cat('FELIX')

# now lets call in the method speak with both the objects

print(niko.speak())
print(felix.speak())
# NIKO says WOOF!
# FELIX says MEOW!

# So now we have two different classes Dog and Cat and both of them have there own configurations, but both classes
# are using a same method name, i.e. speak(). So this is called polymorphism. Here two different objects are making
# use of same method name and based on the object instance we will use to call them, there values will differ.

# there are multiple ways of showing the use of this polymorphism.
# first way is to iterate through the list of instances we have created for both the classes

for item in [niko, felix]:
    print(item.speak())


# NIKO says WOOF!
# FELIX says MEOW!
# So we can see that with the help of for loop and iterating through the objects of both the classes, we could print two
# different statements. So this is the use of polymorphism.

# another case of using the polymorphism is within the function

def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
# NIKO says WOOF!

pet_speak(felix)


# FELIX says MEOW!

# So this is what polymorphism is, along with its use cases.

# Now more often we make use of inheritance along with abstract classes. Abstract classes are the classes which never
# expect to be instantiated. instead its just designed to serve as a base class.

# So lets understand what an abstract class is:

class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract class method")


# Ok so what does this class means, here we have created the __init__ method and then we have also created another
# method speak() but we are not doing anything in it, instead we are expecting that whoever wants to use the method
# speak of this class must inherit the class and override this method according to there own need.from
# and to make sure abstract class must not be instantiated, we have written the statement which will throw up the
# exception that cannot create instance for this class as this is a abstract and you must use this method by overriding
# this method in another class

# So suppose if someone create the instance of this class by mistake, then it must return the exception

# my_animal = Animal('sammy')

# print(my_animal.speak())
# NotImplementedError: Subclass must implement this abstract class method

# So basically this is not allowed as this is a abstract class
# So let us override this method speak as expected by the abstract class into another classes Dog and Cat

class Dog(Animal):

    def speak(self):
        return self.name + " says Woof"


class Cat(Animal):

    def speak(self):
        return self.name + " Says MEOW"


fido = Dog('fido')
print(fido.speak())
# fido says Woof
isis = Cat('isis')
print(isis.speak())
# isis Says MEOW


