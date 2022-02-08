class Foo:

    @staticmethod
    def bar(x):
        """bar() can be called without instantiating from Foo"""
        print(x, "on class")

    def nbar(self, x):
        """nbar() can be used on an instance of Foo"""
        print(x, "on ", self)

Foo.bar("Call of bar on class")
# Foo.nbar("call on class")  -- TypeError: Foo.nbar() missing 1 required positional argument: 'x'
Foo.nbar(Foo, "Call of nbar on class")

foo = Foo()
foo.bar("Call of bar on instance")
foo.nbar("Call of nbar on instance")