class Foo:

    @staticmethod
    def bar(x):
        """bar() can be called without instantiating from Foo"""
        print(x)

    def nbar(self, x):
        """nbar() can be used on an instance of Foo"""
        print(x)

Foo.bar("bar")
Foo.nbar(Foo,"nbar")

foo = Foo()
foo.bar("instance bar")
foo.nbar("instance nbar")