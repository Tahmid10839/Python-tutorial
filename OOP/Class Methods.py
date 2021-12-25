
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


Tahmid = Employee("Tahmid",10000)
Rahim = Employee("Rahim",20000)
Tahmid.change_leaves(35)
print(Tahmid.details())
print(Tahmid.salary)
Rahim.change_leaves(10)
print(Rahim.details())