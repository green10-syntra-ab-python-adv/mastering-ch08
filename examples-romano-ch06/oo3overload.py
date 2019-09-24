from typing import overload
from typing import Any, Optional
class A(object):
    @overload
    def stackoverflow(self) -> None:
        print('first method blabla')
    @overload
    def stackoverflow(self, i: Any) -> None:
        print('second method blabla', i)
    def stackoverflow(self, i: Optional[Any] = None) -> None:
        if not i:
            print('first method')
        else:
            print('second method', i)

ob=A()
ob.stackoverflow(2)