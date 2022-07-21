# overriding---> run time polymorphism

class A:

    def __init__(self):
        print("a")
    def m1(self):
        print("m1")
class B(A):
    def m1(self):
        print("overrided")

ob=B()
ob.m1()