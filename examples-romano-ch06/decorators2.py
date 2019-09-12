
from time import sleep, time


def f():
    sleep(.3)


def g():
    sleep(.5)


def measure(func):
    """ Measure execution time of function

    :param func: the function whoose performance needs to be measured
    :return: the execution time
    """
    t = time()
    func()
    print(func.__name__, "took:", time() - t)


measure(f)
measure(g)

""" Output:

f took: 0.30040740966796875
g took: 0.500760555267334
"""

