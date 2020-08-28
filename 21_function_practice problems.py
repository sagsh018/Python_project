# Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if
# one or both numbers are odd¶
# solution
# =========
def greater_check(x, y):
    if x > y:
        return x
    else:
        return y


def smaller_check(x, y):
    if x < y:
        return x
    else:
        return y


def even_odd_check(x, y):
    if x % 2 == 0 and y % 2 == 0:
        return greater_check(x, y)
    else:
        return smaller_check(x, y)


print(even_odd_check(2, 4))
# 4
print(even_odd_check(1, 4))
# 1
print(even_odd_check(2, 5))
# 2
print(even_odd_check(3, 7))


# 3


# Write a function takes a two-word string and returns True if both words begin with same letter
# solution
# ========
def begin_same(str):
    my_list = str.split()
    print(my_list)
    if my_list[0][0] == my_list[1][0]:
        return True
    else:
        return False


print(begin_same('come comedfsdf'))


# ['come', 'comedfsdf']
# True


# Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# solution
def makes_twenty(num1, num2):
    if num1 + num2 == 20:
        return True
    elif num1 == 20 or num2 == 20:
        return True
    else:
        return False


print(makes_twenty(20, 10))
# True
print(makes_twenty(12, 8))
# True
print(makes_twenty(2, 3))


# False

# Write a function that capitalizes the first and fourth letters of a name
# solution
def letter_cap(name):
    new_string = name[:3].capitalize() + name[3:].capitalize()
    return new_string


print(letter_cap('macdonald'))


# Given an integer n, return True if n is within 10 of either 100 or 200
# solution
# =========

def almost_there(num):
    if num in range(91, 111) or num in range(191, 211):
        return True
    else:
        return False


print(almost_there(104))
# True
print(almost_there(150))
# False
print(almost_there(209))


# True

# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# solution
# =========

def side_by_side(my_list):
    flag = False
    for index, value in enumerate(my_list):
        # print(index, value)
        if my_list[index] == my_list[index + 1] == 3:
            flag = True
            break
        elif index + 1 == len(my_list) - 1:
            break
        else:
            pass
    return flag


print(side_by_side([1, 3, 3]))
# True
print(side_by_side([1, 3, 1, 3]))
# False
print(side_by_side([3, 1, 3]))


# Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
def paper_doll(name):
    temp = ''
    for x in name:
        temp = temp + 3 * x
    return temp

print(paper_doll('Hello'))
# HHHeeellllllooo

print(paper_doll('Mississippi'))
# MMMiiissssssiiissssssiiippppppiii



