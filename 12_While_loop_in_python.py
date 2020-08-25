# While loop will continue to execute a block of code while some condition remains true
# Syntax
# ===============================
#   while some_boolean_condition:
#       do something
# ===============================
# We can also combine while statement with the else statement
# ===============================
#   while some_boolean_condition:
#       do something
#   else:
#       So something else
# ===============================

# example
# =======
x = 0
while x < 5:
    print(f'Value of x {x+1}th time is : {x}')
    x += 1
else:
    print(f'{x+1}th time x is not less than 5')
# Value of x 1th time is : 0
# Value of x 2th time is : 1
# Value of x 3th time is : 2
# Value of x 4th time is : 3
# Value of x 5th time is : 4
# 6th time x is not less than 5

# break, continue, pass
# ======================
# break : breaks out of the current closest enclosing loop
# continue : Goes to the top of the closest enclosing loop
# pass: does absolutely nothing

# pass
# ====
new_list = [1, 2, 3]
for item in new_list:
    pass
# This will do nothing but it will not throw error because python do expect us to write something and we can't leave
# that blank. So this is a use of pass keyword. We often use it while declaring the functions. when we don't want
# to define whats goes inside the function immediately

# continue
# =========
for letter in 'sammy':
    print(letter)
# s
# a
# m
# m
# y
# Suppose we don't want to print letter a in sammy, then we will use continue here
for letter in 'Sammy':
    if letter == 'a':
        continue
    print(letter)
# S
# m
# m
# y

# break
# ======
# suppose we want to print letters of word sammy until letter a occurs
for letter in 'sammy':
    if letter == 'a':
        break
    print(letter)
# s
# break is more useful with while loop. lets see the example of while loop along with break statement
x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
# 0
# 1









