import functools, time



def example_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("A decorator was applied to %s " % func)
        value = func(*args, **kwargs) + " decorated to serve you"
        return value
    return wrapper

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print("Finished %s in %.9f secs" % (func, run_time) )
        return value
    return wrapper_timer


@timer
@example_decorator
def example(number1, number2):
    return "hi sum " + str(number1+number2)

print ( example(4,3) )