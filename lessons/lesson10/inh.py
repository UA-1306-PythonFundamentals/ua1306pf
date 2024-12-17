class A:
    def foo(self):
        print("A.foo")
    pass
class B:
    pass
class C:
    def foo(self):
        print("C.foo")
class D(A, B):
    pass
class E(B, C):
    pass
class F(C, E, D):
    pass


# f = F()

# f.foo()
# print(F.__mro__)