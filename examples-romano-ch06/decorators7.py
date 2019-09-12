
from time import sleep, time

from functools import wraps


def announce(func):
    def wrapper(*args, **kwargs):
        print("+---------------------------------------------------+ ")
        print("| And now let's see an example using two decorators | ")
        print("|                                                   | ")
        func(*args, **kwargs)
        print("|                                                   | ")
        print("+---------------------------------------------------+ ")
    return wrapper


def measure(unit):
    """ Measure execution time of function


    :param unit: the unit of the measurement
    :return: the decorator
    """
    def decorator(func):
        """ Decorate func

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
            print("|      ", func.__name__, "took:", time() - t, unit, "        |")

        return wrapper
    return decorator


@announce
@measure("seconds")
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


""" Output:

+---------------------------------------------------+ 
| And now let's see an example using two decorators | 
|                                                   | 
|       f took: 0.2002274990081787 seconds          |
|                                                   | 
+---------------------------------------------------+ 
+---------------------------------------------------+ 
| And now let's see an example using two decorators | 
|                                                   | 
|       f took: 0.30027127265930176 seconds         |
|                                                   | 
+---------------------------------------------------+ 
wrapper
"""

