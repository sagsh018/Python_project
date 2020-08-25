# In This lecture we are going to learn how to chain the comparison operators we have learnt in the previous lecture
# We can chain the comparison operator with the help of below listed logical operators
# and
# or
# not

# Suppose we want to do two comparisons
print(1 < 2)
# True
print(2 < 3)
# True
# another way of doing them in same line is
print(1 < 2 < 3)
# True
# Now this is returning true because it is checking whether 1 is less than 2 and also whether 2 is less than 3
print(1 < 2 > 3)
# False, as second condition failed
# This same thing can be done with logical operator "and"
print((1 < 2) and (2 < 3))
# True
print((1 < 2) and (2 > 3))
# False
# Also we can do the same in case of character and string with all the comparison operators
print(('h' == 'h') and (2 == 2))
# Ture
# So basically and logical operator follows below concept
# T and T = T
# T and F = F
# F and T = F
# F and F = F

# or
# ===
print((1 < 2) or (2 < 3))
# True
print((1 < 2) or (3 < 2))
# True
print((2 < 1) or (2 < 3))
# True
print((2 > 3) or (4 < 3))
# False
# or follows below rules
# T or T = T
# T or F = T
# F or T = T
# F or F = F

# not
# ====
print(1 == 1)
# True
print(not 1 == 1)
# False
# not follows below rules
# not T = F
# not F = T


