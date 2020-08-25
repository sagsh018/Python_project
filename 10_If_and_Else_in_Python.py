# Here we are going to discuss about if, elif and else statement
# Used for controlling the flow of login
# keywords
# if
# else
# elif
# Also note that control flow statements in python follows colons and indentations
# Syntax

# ====================
# if some_condition:
#   execute some code
# ====================

# ====================
# if some_condition:
#   execute some_code
# else:
#   Do something else
# =====================

# ========================
# if some_condition:
#   execute some_code
# elif some_other_condition:
#   execute some_other_code
# else:
#   execute something else
# ========================

# example

if True:
    print('ITS TRUE!')
# ITS TRUE!

hungry = True
if hungry:
    print('Feed ME!')
# Feed ME!

hungry = False
if hungry:
    print('Feed Me')
# This will not print anything

hungry = False
if hungry:
    print('Feed Me!')
else:
    print('I am not hungry')
# I am not hungry

hungry = True
if hungry:
    print('Feed Me!')
else:
    print('I am not hungry')
# Feed Me!

loc = 'Auto Shop'
if loc == 'Auto Shop':
    print('We are at auto shop')
elif loc == 'Store':
    print('We are at Store')
elif loc == 'Bank':
    print('We are at bank')
else:
    print("We don't know this location")
# We are at auto shop


