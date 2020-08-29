import string


# Write a function that computes the volume of a sphere given its radius.

def sphere_vol(radius):
    return (4 / 3) * 3.14 * (radius ** 3)


print(sphere_vol(2))


# 33.49333333333333

# Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(high, low, num):
    if num in range(low, high + 1):
        return True


print(ran_check(10, 0, 10))
# True

print(ran_check(7, 2, 5))


# True

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters
def up_low(s):
    uppercase = 0
    lowercase = 0
    my_list = list(s)
    print(my_list)
    for letter in my_list:
        if letter.isupper() and letter != ' ':
            uppercase += 1
        elif letter.islower() and letter != ' ':
            lowercase += 1
        else:
            pass
    print(f'No. of uppercase letter are {uppercase}')
    print(f'No. of lowercase letter are {lowercase}')


up_low('Hello Mr. Rogers, how are you this fine Tuesday?')


# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(my_list):
    s = set()
    s = set(my_list)
    temp_list = []
    for letter in s:
        temp_list.append(letter)
    return temp_list


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))


# [1, 2, 3, 4, 5]


# Write a Python function to multiply all the numbers in a list.

def multiply(my_list):
    temp = 1
    for num in my_list:
        temp *= num

    return temp


print(multiply([1, 2, 3, -4]))


# Write a Python function that checks whether a passed in string is palindrome or not.

def check_palin(s):
    s = s.replace(' ', '')
    if s == s[::-1]:
        return True
    else:
        return False


print(check_palin('nurses rusdfsn'))
# False


print(string.ascii_lowercase)
# abcdefghijklmnopqrstuvwxyz

str = "The quick brown fox jumps over the lazy dog"
str = str.replace(' ', '')

str1 = set(str)
print(str1)


def ispangram(str1, alphabet=string.ascii_lowercase):
    flag = False
    str1 = str1.replace(' ', '')
    s = set(str1.lower())
    for item in alphabet:
        if item in s:
            flag = True
        else:
            flag = False
            break
    return flag


print(ispangram('The quick brown fox jumps over the lazy dog'))
# True
print(ispangram('The quick brown fox jumps over the lazy'))
# False





