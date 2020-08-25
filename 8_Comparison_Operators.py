# Here we will learn how to use comparison operators and how we can return boolean values with the help of that.
# Below is the list of operators :
# "==" : returns true if two operands are equal
# "!=" : returns true if two operands are not equal
# ">" : return true if left operand is greater than right operand
# "<" : return true if left operand is greater than right operand
# ">=" : return true if left operand is greater or equal to right operand
# "<=" : return true if left operand is less than or equal to right operand.

# "=="
# Lets take up the examples for quality operator
print(2 == 2)
# True
print(2 == 1)
# False
print('Hello' == 'Bye')
# False
print('Bye' == 'bye')
# False, Notice capitalization is counted for equality
print('2' == 2)
# False, Notice data type also counted while checking the equality
print(2.0 == 2)
# True, Floating point numbers, as long as they hold the same value it returns true as above case.

# "!="
# ====
print(3 != 3)
# False
print(3 != 4)
# True

# "<"
# ====
print(1 < 2)
# True
print(2 < 1)
# False

# ">"
# =====
print(1 > 2)
# False
print(2 > 1)
# True

# ">="
# =====
print(2 >= 2)
# True
print(4 >= 1)
# True
print(4 >= 8)
# False

# "<="
# ====
print(2 <= 2)
# True
print(2 <= 1)
# False


