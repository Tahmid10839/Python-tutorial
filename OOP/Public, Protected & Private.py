
class Employee:
    no_of_leaves = 8
    _protect = 7
    __private = 6
    def __init__(self,aname,asalary):
        self.name = aname
        self.salary = asalary
    def details(self):
        return f"Name: {self.name} \nSalary: {self.salary} \nNo of leaves: {self.no_of_leaves}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good",string)

Tahmid = Employee("Tahmid",60000)
print(Tahmid._protect)
print(Tahmid._Employee__private)