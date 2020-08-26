# Lets discuss the functions with complex logic

# Lets write the function to check if the number is even or not

def check_even(num):
    if num % 2 == 0:
        print('Number is even')
    else:
        print('number is odd')


check_even(2)
# Number is even
check_even(33)


# number is odd


# We could also write this function check if the number is even return true otherwise return false

def another_even_check(num):
    return num % 2 == 0


result = another_even_check(2)
print(result)


# True

# Now lets create a function check, which element inside the list is even and which is odd
def list_even_check(my_list):
    for x in my_list:
        if x % 2 == 0:
            print(f'Number {x} is even')
        else:
            print(f'Number {x} is odd')


list_even_check([1, 2, 3, 4, 5])


# Number 1 is odd
# Number 2 is even
# Number 3 is odd
# Number 4 is even
# Number 5 is odd


# Suppose we want to create a function that should return true if there is any even number inside the list
# and return false if there is no even number inside the list

def list_even_check(my_list):
    for num in my_list:
        if num % 2 == 0:
            return True
        else:
            pass
    return False  # Notice that this return statement is kept outside the if statement inside for loop.
    # So that if in case first odd number comes, then it should not return false even though there is
    # even number at the end of list


print(list_even_check([1, 2, 3, 4, 5]))
# True
print(list_even_check([1, 3, 5]))
# False
print(list_even_check([1, 3, 5, 7, 8]))


# True

# Now suppose we want to write a function to create a list of even numbers from the given list
def list_even_check(my_list):
    new_list = []
    for num in my_list:
        if num % 2 == 0:
            new_list.append(num)
        else:
            pass
    return new_list


print(list_even_check([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
[2, 4, 6, 8, 10, 12, 14, 16]

