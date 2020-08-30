# So int this lecture we are going to understand the concept behind below type of code
# if __name__ == "__main__"
# and followed by this there is a block of code, which you want to execute
# now if you will notice this above line here, "__name__" is a built in variable for particular .py script. and
# when we run that particular .py script directly from the console or from IDE or from command line that __name__
# is assigned the special script value which is "__main__"
#
# So with this way we could know that if __name__ is equal to "__main__" then this is the script called direclty from
# command line from from IDE or from console and it is this script from where rest of the modules or packages are
# imported and ran

# So to understand this we will do small demo
# lets create two .py files under our working directory : /c/Users/Sagar/projects/Python_project
# 1) one.py
# ==========================================
# def func():
#     print("FUNC() at top level in ONE.PY")
#
#
# print("TOP LEVEL IN ONE.PY")
#
# if __name__ == "__main__":
#     print("ONE.PY is run directly")
# else:
#     print("ONE.PY is imported")
# ============================================
#
# similarly lets create another .py script named as two.py
# ==============================================
# import one
#
# print("TOP LEVEL IN TWO.PY")
#
# one.func()
#
# if __name__ == "__main__":
#     print("TWO.PY has been called directly")
# else:
#     print("TWO.PY has been imported")
# ==============================================
# So now save both the file and run them one by one
# if we run ONE.py first
# ==========================
# TOP LEVEL IN ONE.PY
# ONE.PY is run directly
# ==========================
#
# if we run two.py first
# ========================
# TOP LEVEL IN ONE.PY
# ONE.PY is imported
# TOP LEVEL IN TWO.PY
# FUNC() at top level in ONE.PY
# TWO.PY has been called directly
# ================================

# So here in our case we have seen with the help of __name__ == "__main__" which script is called directly.
# but in real life this thing is used more to organise the code in your script

# lets create one more .py script at same level of our working directory
# named as : three.py
# please go inside this file and see the concept

