def foo(a: int, b: float, c: complex, d: dict) -> bool:
    pass


print(foo.__annotations__)

"""prints:

{'b': <class 'float'>, 'return': <class 'bool'>, 'a': <class 'int'>, 
'd': <class 'dict'>, 'c': <class 'complex'>}

"""


def foo2(a: 'ackamarackus', b: ['baboonery', 'balderdash']):
    pass

print(foo2.__annotations__)

"""prints:

{'b': ['baboonery', 'balderdash'], 'a': 'ackamarackus'}
"""


class Codswallop:
    pass


def foo3(c: Codswallop) -> None:
    pass


print(foo3.__annotations__)

"""prints:

{'return': None, 'c': <class '__main__.Codswallop'>}
"""

