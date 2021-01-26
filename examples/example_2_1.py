class Foo:

    @staticmethod
    def bar(x):
        """bar() can be called without instantiating from Foo"""
        print(x, "on class")

    def nbar(self, x):
        """nbar() can be used on an instance of Foo"""
        print(x, "on", self)

Foo.bar("class bar")
# Foo.nbar("class nbar")
# Foo.nbar(Foo, "class nbar")

foo = Foo()
foo.bar("instance bar")
foo.nbar("instance nbar")