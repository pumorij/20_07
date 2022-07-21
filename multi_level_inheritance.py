# multi level inheritance

class A():
    def f(self):
        a=10
        print(a)
class B(A):
    def g(self):
        b=20
        print(b)
class C(B):
    def h(self):
        c=30
        print(c)
ob=C()
ob.f()
ob.g()
ob.h()