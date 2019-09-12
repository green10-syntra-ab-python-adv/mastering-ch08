import functools


def example_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("A decorator was applied to %s " % func)
        value = func(*args, **kwargs) + " decorated to serve you"
        return value
    return wrapper


@example_decorator
def example(number1, number2):
    return "hi sum " + str(number1+number2)

print ( example(4,3) )