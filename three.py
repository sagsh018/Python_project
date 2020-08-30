def func_3():
    print("This should be printed 3rd")


def func_2():
    print("This should be printed 2nd")


def func_1():
    print("Ths should be printed 1st")


if __name__ == "__main__":
    func_1()
    func_2()
    func_3()

# Ths should be printed 1st
# This should be printed 2nd
# This should be printed 3rd
# So as we can see that even though we have defined all the functions at top level indentaton of our .py script but
# they have executed in the order we have written in the if condition check.
