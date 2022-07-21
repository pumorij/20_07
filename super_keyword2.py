# implementation of super keyword

class A():
    a=10
    b=20
    def __init__(self,a,b):
        print("a")
    def m1(self):
        print("m1")

class B(A):
    a=4
    b=5
    def __init__(self):
        super().__init__(2,12)
    def m2(self):
        super().m1()
        print(self.a,self.b)
        print(super().a,super().b)

ob=B()
ob.m1()
ob.m2()