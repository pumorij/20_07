# multiple inheritance

class A:
    def f(self):
        a=10
        print(a)
class B:
    def g(self):
        b=20
        print(b)

class C(A,B):
    def h(self):
        c=30
        print(c)
ob=C()
ob.h()
ob.g()
ob.f()