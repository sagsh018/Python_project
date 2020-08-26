# in this lecture we are going to learn more about function, and returning multiple items from function using tuple
# unpacking
# Suppose we want to write a function, which takes in a list of tuples having name of employee and number of hrs worked
# We have to decide who is the employee of the month based number of hours employee worked. so highest number of hours
# more chances of wining.
# notice that we need to return the name of the employee who worked the most(in short employee of the month along with
# number of hours he worked
my_list = [('vivek', 200), ('sahil', 300), ('ramya', 500)]
print(my_list)


# [('vivek', 200), ('sahil', 300), ('ramya', 500)]

def emp_of_month(my_list):
    for item in my_list:
        print(item)


emp_of_month(my_list)


# ('vivek', 200)
# ('sahil', 300)
# ('ramya', 500)

# Now lets tuple unpacking into consideration
def emp_of_month(my_list):
    for emp, hrs in my_list:
        print(f'{emp} worked for {hrs} this month')


emp_of_month(my_list)


# vivek worked for 200 this month
# sahil worked for 300 this month
# ramya worked for 500 this month


# now lets write a function who worked for maximum hours in office for the month

def emp_of_month(my_list):
    hours = 0
    employee = ''
    for emp, hrs in my_list:
        if hrs > hours:
            hours = hrs
            employee = emp
        else:
            pass
    return employee, hours


no_of_emp = int(input('Please enter how many employees do you have : '))
x = 1
my_list = []
while x <= no_of_emp:
    emp_name = input('Enter emp name : ')
    hours_detail = int(input('Enter his hours details : '))
    my_list.append((emp_name, hours_detail))
    x += 1
print(f'Employees detail you have entered : {my_list}')
choice = input('Is the information entered by you correct (yes/no) : ')
if choice == 'yes':
    name, hour = emp_of_month(my_list) # So here we are doing tuple unpacking with what is returned by a function
    print(f'Employee of the month is {name} and he worked for {hour} hours')
else:
    print('Thanks for entering the details but you choose to discontinue')

# Notice that we did tuple unpacking here inside the function definition as well as while calling it.
# but during calling function, if you are not sure how many values does function returns, then its always a better
# option to store the function value first into single variable and then explore that first.
