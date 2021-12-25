
class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside A's Constructor"
        self.classvar1 = "Instance var in class A"


class B(A):
    classvar1 = "I am in class B"
    def __init__(self):
        self.var1 = "I am inside B's constructor"
        self.classvar1 = "Instance var in class B"
        super().__init__()
        print(super().classvar1)


a = A()
b = B()

print(b.classvar1)