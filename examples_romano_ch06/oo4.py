"""Following PEP-0443

Therefore, this PEP proposes a uniform API to address
dynamic overloading using decorators.
"""

from functools import singledispatch


@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)


@fun.register(int)
def _(arg, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)


@fun.register(list)
def _(arg, verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)


fun(1.1, True)
fun(11, True)
fun(["een", "twee"], True)
fun(complex(1,2), True)









