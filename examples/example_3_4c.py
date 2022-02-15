from __future__ import annotations


class A:
    def do_smth_with_b(self, a_b: B):
        print("Class A object doing something with a class B object")


class B:
    def do_smth_with_a(self, an_a: A):
        print("Class B object doing something with a class A object")


a = A()
b = B()

a.do_smth_with_b(b)
b.do_smth_with_a(a)
