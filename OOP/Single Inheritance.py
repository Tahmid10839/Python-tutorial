
class Employee:
    no_of_leaves = 8
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

class Programmer(Employee):
    def __init__(self, aname, asalary,languages):
        self.name = aname
        self.salary = asalary
        self.languages = languages
    def printprog(self):
        return f"Name: {self.name} \nSalary: {self.salary} \nNo of leaves: {self.no_of_leaves} \nLanguages: {self.languages}"


Tahmid = Employee("Tahmid",10000)
Rahim = Employee("Rahim",20000)
Karim = Employee.from_str("Karim-150000")

Abar = Programmer("Abar",300000,['Python','C++'])

print(Abar.printprog())



