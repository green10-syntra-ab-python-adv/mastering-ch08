
from time import sleep, time

from functools import wraps


def measure(func):
    """ Measure execution time of function

    :param func: the function whoose performance needs to be measured
    :return: the function func, wrapped with execution time measurement capability
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        """ Define wrapped function,

        The wrapped function executes the function func and measures execution time

        :param args: any number of positional arguments, to be passed by func
        :param kwargs: any number of keyword arguments, to be passed to func
        :return: wrapped function
        """
        t = time()
        func(*args, **kwargs)
        print(func.__name__, "took:", time() - t)

    return wrapper


@measure
def f(sleep_time=0.1):
    """ Sleep a given amount of time

    Function is 'decorated' with the @measure decorator
    giving it the capability to measure its execution time

    :param sleep_time: the amount of time to sleep
    """
    sleep(sleep_time)


f(0.2)
f(sleep_time=0.3)
print(f.__name__)
print(f.__doc__.split("\n")[0])  # print first line of docstring


""" Output:

f took: 0.2003176212310791
f took: 0.3003554344177246
f
 Sleep a given amount of time
"""

