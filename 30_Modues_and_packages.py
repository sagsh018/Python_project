# So in this module we are going to understand how to create our own modules and packages
# Essentially modules are just the .py scripts that you call in another .py script
# whereas packages are collection of modules. however there is a key.py script called __init__.py that needs to be
# placed inside the folder to let know python know that this collection of .py script should be treated as  a
# python package
# So here we are going to create two files one is the module file we will call in our .py script and we will place it
# in following location : /c/Users/Sagar/projects/Python_project
# So lets create another module .py "mymodule.py" script in above location
# And we will also create another .py script where we will call in this module .py file. and we will name our .py
# script as "myprogram.py"
# So lets open up mymodule.py and write the below code to that  file
# ==========================================
# def my_func():
#     print("I am currently in mymodule.py")
# ===========================================
# Then save this
# So here if we notice this technique of creating different modules and segregate the code into different module
# files instead of putting it into one file and then calling it in our own .py script when we need it.
# and collection of such module files, will become the package or library
# Now lets move on to myprogram.py file and lets try to use the module file in our program.
# ===========================================
# from mymodule import my_func
#
# my_func()
# ============================================
# so save it and run the file myprogram.py and you will see the below output
# I am currently in mymodule.py
# So this is how we can import function defined in some other .py script which is mymodule.py file into our program.
# Now sometime even this segregation of code between different module also become cumbersome. so for that we can even
# combine different modules into folders and make them as packages

# So lets go ahead and create one folder under my working directory /c/Users/Sagar/projects/Python_project
# folder name : MyMainPackage
# and inside this folder lets create another sub folder named  as : SubPackage
# So we have this king of package and sub package
# /c/Users/Sagar/projects/Python_project/MyMainPackage/SubPackage
# but these are just the directories created on a windows OS, to make python understand that these are the packages
# we will have to create one .py file inside both the folders named as "__init__py"
# So there are two files under both the folders as below
# /c/Users/Sagar/projects/Python_project/MyMainPackage/SubPackage/__init__.py
# /c/Users/Sagar/projects/Python_project/MyMainPackage/__init__.py
# Now notice that you don't have to write anything in these files. They just need to be there in this folders,
# so that when pythin search here and find them, it can understand that these are not the normal directories, but these
# are the packages
# now we are going to create two more files and both will act as a .py scripts inside my Main package and sub package
# where we will call out modules and packages
# So these are the files
# /c/Users/Sagar/projects/Python_project/MyMainPackage/SubPackage/mysubscript.py
# /c/Users/Sagar/projects/Python_project/MyMainPackage/mymainscript.py
# So now total we have 4 files
# /c/Users/Sagar/projects/Python_project/mymodule.py
# def my_func():
#     print("I am currently in my_module")

# /c/Users/Sagar/projects/Python_project/myprogram.py
# from mymodule import my_func
#
# my_func()

# /c/Users/Sagar/projects/Python_project/MyMainPackage/mymainscript.py
# content in this file
# def main_script():
#     print("Hey i am function from mymainscript in Main package")

# /c/Users/Sagar/projects/Python_project/MyMainPackage/SubPackage/mysubscript.py
# def sub_script():
#     print("Hey i am function from mysubscript in sub package")

# So we have entire structure of modules and packages here in our local system.
# Notice that we are going to call and import modules or packages in our main program myprogram.py
# and we would like python to run this file first as a main program
# So lets update our myprogram.py file as below
# ===================================================
# from MyMainPackage import mymainscript
# from MyMainPackage.SubPackage import  mysubscript
# ====================================================
# So this is how we could import the module from package and subpackage. we could even go further and import directly
# the function inside the modules
# now once we have have imported the modules from both the package and sub package in our main program, lets try to use
# the function of those modules in out main program
# ====================================================
# from MyMainPackage import mymainscript
# from MyMainPackage.SubPackage import mysubscript
#
# mymainscript.main_script()
# # Hey i am function from mymainscript in Main package
#
# mysubscript.sub_script()
# #  Hey i am function from mysubscript in sub package
# =====================================================
# So we can see that we have outputs from the functions inside the modules which are present in package and sub package



