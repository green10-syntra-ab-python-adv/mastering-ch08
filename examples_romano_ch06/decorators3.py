
from time import sleep, time


def f(sleep_time=0.1):
    """ Sleep a given amount of time

    :param sleep_time: the amount of time to sleep
    """
    sleep(sleep_time)


def measure(func, *args, **kwargs):
    """ Measure execution time of function

    :param func: the function whoose performance needs to be measured
    :param args: any number of positional arguments, to be passed by func
    :param kwargs: any number of keyword arguments, to be passed to func
    :return: the execution time
    """
    t = time()
    func(*args, **kwargs)
    print(func.__name__, "took:", time() - t)


measure(f, sleep_time=0.2)
measure(f, 0.3)

""" Output:

f took: 0.2004384994506836
f took: 0.3005964756011963
"""

