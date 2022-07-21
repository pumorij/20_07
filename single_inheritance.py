# single inheritance

class A:
    def a(self):
        a=10
        print(a)
class B(A):
    def b(self):
        b=20
        print(b)

ob=B()
ob.a()
ob.b()
    