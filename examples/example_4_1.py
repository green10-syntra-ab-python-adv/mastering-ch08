import contextlib

def some_action():
    print("This function can be called in the block")
    print("It serves as yield")

@contextlib.contextmanager
def before_and_after():
    print("Before")
    try:
        yield some_action
        # there are no multiline lambda's!
    finally:
        print("After")

with before_and_after() as f:
    print("When I call f(), I get:")
    f()
    print("I can do other things too in the block")
