# heirarchial inheritance

class base():
    def f1(self):
        print("Base Class")
class derived1(base):
    def f2(self):
        print("Derived Class 1")
class derived2(base):
    def f3(self):
        print("Derived Class 2")

ob=derived1()
ob.f2()
ob.f1()