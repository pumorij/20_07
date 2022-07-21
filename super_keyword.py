# super keyword

class A():
    a=10
    b=20
    def __init__(self):
        print("A")
    def m1(self):
        print("m")
class B(A):
    a=5
    b=4
    def m2(self):
        print(self.a,self.b)
        print(super().a+super().b)

ob=B()
ob.m1()
ob.m2()