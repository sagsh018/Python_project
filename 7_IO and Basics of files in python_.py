# Files
# ========
# So for this first we have to create a normal Text file in order to play around with that.
# Suppose we have opened one file named as my_file.txt in the same location we are working in and write some data into
# it.
# Data
# =====
# Hello This is a Test file
# This is a first line
# This is a second line
# This is a third line
# Save this file, once this is ready we can play around with it.

# So first in order to work with file we will have to open up the file
my_file = open('my_file.txt')
# So this will open up a file for us to work with.

# Notice that there could be a chance of having error of file not found or no such file or directory which is a
# common error number 2. This could happen only in two cases.
# a) if you pass wrong file name in the open command as below
# my_file = open('whoops_wrong_file.txt')
# [Errno 2] No such file or directory: 'whoops_wrong_file.txt'
# b) if by chance we actually didn't provided correct file path
# So for now are assuming that we have our text file in our python working directory only and is correctly placed.
# Now we can make use of various function related to file operations

print(my_file.read())
# Hello This is a Test file
# This is a first line
# This is a second line
# This is a third line

# Suppose if you try to read the file again
print(my_file.read())
# This time you won't get any text. The reason is the pointer is now pointing to the end of file which needs to
# be seek back to the starting.
print(my_file.seek(0))
# 0, so this shows that our file pointer/cursor is at 0 again. now we can read the file again.

print(type(my_file))
# <class '_io.TextIOWrapper'>
# we can also save the content we read from the file
content = my_file.read()
print(content)
# Hello This is a Test file
# This is a first line
# This is a second line
# This is a third line
print(type(content))
# <class 'str'>
# so that means when we tried to store the date inside a file in a variable, it is stored as a string.

# There is another way of reading the file and making each line of a file an element of a list in python
# This could be done using method readlines()
my_file.seek(0)
print(my_file.readlines())
# ['Hello This is a Test file\n', 'This is a first line\n', 'This is a second line\n', 'This is a third line']

my_file.seek(0)
file_list = my_file.readlines()
print(file_list)
my_file.seek(0)
# ['Hello This is a Test file\n', 'This is a first line\n', 'This is a second line\n', 'This is a third line']
# '\n' is indicating that there is a new line after this
# now since file_list is a list, we can all the operations on the file data which we can do on the lists
# print(file_list[0])
# Hello This is a Test file
# best practice for opening a file is to close the file after working on it, in order to avoid inconsistency
my_file.close()

# Now suppose you are trying to open up a file which is not in the current location as that of your working
# directory.
# in that case, while opening the file you have to provide the absolute path.
# Suppose we have created another text file named as new_file.txt, at same location of our working directory.
# but this time we will open the file with absolute path

my_file = open("C:\\Users\\Sagar\\projects\\Python_project\\new_file")
print(my_file.readlines())
# ['This is a normal Test file\n', 'This is going to be used to test the file operations\n', 'Sit back and play with
# this file']
# So lets close this file as well
my_file.close()
# my_file.seek(0)
# my_file.read()
# ValueError: I/O operation on closed file. This is because the file is closed now.

# Now since we have to always keep in mind to close the file after work. So lets learn the new technique to open the
# file. so that we don't need to worry about closing the file after useing it.

with open('new_file') as my_file:
    content = my_file.readlines()

# ['This is a normal Test file\n', 'This is going to be used to test the file operations\n', 'Sit back and play with
# this file']

print(type(content))
# <class 'list'>

# reading and writing through files
# =================================

with open('my_file.txt', mode='r') as my_file:
    content = my_file.read()
print(content)
# Hello This is a Test file
# This is a first line
# This is a second line
# This is a third line

# Now consider below piece of code
with open('new_file', mode='r') as my_new_file:
    content = my_new_file.read()
print(content)
# This is a normal Test file
# This is going to be used to test the file operations
# Sit back and play with this file

# Now if we open the same file to read with the write mode
# with open('new_file', mode='w') as my_new_file:
#    content = my_new_file.read()
# print(content)
# io.UnsupportedOperation: not readable. Since we have opned the file for writing and we are trying to read the file.
# this kind of operations is not supported

# Reading, Writing, Appending modes
# mode = 'r' == is a read only mode
# mode = 'w' == is a write only mode (will overwrite files or create a new one, if file does not exist)
# mode = 'a' == is a append only mode ( will add on the lines to the file)
# mode = 'r+' == is for reading and writing
# mode = 'w+' == is for writing and reading ( again it overwrite the file and cretes a new file if does not exist)

# So lets play with these modes.
# suppose we have created another text file named as final.txt

with open('final.txt', mode='r') as my_new_file:
    print(my_new_file.read())
# ONE ON FIRST
# TWO ON SECOND
# THREE ON THIRD

# Suppose i want to add new line to this file

with open('final.txt', mode='a') as f:
    f.write('\nFOUR ON FOURTH')

with open('final.txt', 'r') as f:
    print(f.read())
# ONE ON FIRST
# TWO ON SECOND
# THREE ON THIRD
# FOUR ON FOURTH

# Now lets open up a file which does not exist with the 'w' mode, so its going to create file

with open('XYX.txt', mode='w') as f:
    f.write('Created while checking write mode')

with open('XYX.txt', mode='r') as f:
    print(f.read())
# Created while checking write mode







