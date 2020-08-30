# in this lecture we are going to talk about PyPi with Pip install
# PyPI is a repository for open source third party python packages
# So far in this course we have taken a look at the builtin libraries which are also called as standard libraries
# but there are many other libraries available that people have open sourced and shared on PiPI and these are
# also called as packages
# we could use pip install at the command line to install these packages
# We have already installed pip while installing the python from python.org
# so with the help of pip we could easily download the packages from the PyPi repository

# So now with the help of pip we will learn how to download the packages from pypi repo.  We will be using terminal
# for using pip

# so lets start by installing the "requests" package which is used to request information from sites online.
# pip install requests -- Type this in git bash
# So this command will show you that request is already installed as part of anaconda distribution installation

# Lets try to install another library/package used to have colorized output on terminal
# pip install colorama
# =========================================================
# Collecting colorama
#   Downloading colorama-0.4.3-py2.py3-none-any.whl (15 kB)
# Installing collected packages: colorama
# Successfully installed colorama-0.4.3
# ==========================================================
# So above of the ouput of the command on git bash and it shows that our package colorama is installed
# on the terminal itself we can go into debug/python concole mode and run this package
# =================commands on python console==========================
# from colorama import init ==> This is to import first the init() method of this package to make the environment ready
# init()
# from colorama import Fore ==> Then we are importing the Fore which stands for foreground
# print(Fore.RED + "This is Red Test")
# This is Red Test ==> This text color will look red on python console.
# print(Fore.GREEN + "Switching to green color")
# ======================================================================

# Now to check or download the required packages/libraries we can simply make a google search as below
# search string on google ==> "python package for <name for which you require the package>"
# ex: python package for excel
# let search it on google
# We will go on the first link for https://www.python-excel.org/
# and this will list all the available packages to work with excel files in python
# and along with all the packages there will be links to download, documentation, etc
# lets go to the download link for one of the package called as openpyxl
# https://pypi.org/project/openpyxl/
# Now this will have information on how to install this package  and how to use it in our codes
# So lets install this frist
# pip install openpyxl
# once that is  downloaded, you can easily import the openpyxl into your code with below statement
# import openpyxl

# So this all about the basics of pip install and how to download the external libraries and packages and
# using them inside our code using import statements
