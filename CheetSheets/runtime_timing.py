import  inspect
from time import time


def timer_example(func):
    def f(x, y=10):
        before = time()
        rv = func(x, y)
        after = time()
        print('elapsed: ', after-before)
        return rv
    return f

# The @ Symbol is a decorator. It replaces the statement add = timer(add). The function add(...) has
# to follow after the decorator

@timer_example
def add(x,y=10):
    return x + y

@timer_example
def sub(x,y=10):
    return x - y

# print("add(20)", add(20))
# print("add(20, 30)", add(20, 30))
# print("add('a', 'c')", add('a', 'c'))
# print("sub(20)", sub(20))
# print("add(20, 30)", sub(20, 30))

# Different methods to time functions
# from "What Does It Take To Be An Expert At Python?" [https://www.youtube.com/watch?v=7lmCu8wz8ro]


# Will work with any inputs and any functions
def timer(func):
    # from time import time
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print('elapsed: ', after-before)
        return rv
    return f

