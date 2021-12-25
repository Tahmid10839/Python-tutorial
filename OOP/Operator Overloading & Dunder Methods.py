
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
    def __add__(self, other):
        return self.salary+other.salary

    def __truediv__(self, other):
        return self.salary/other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary})"

    def __str__(self):
        return self.details()

Tahmid = Employee("Tahmid",10000)
Rahim = Employee("Rahim",20000)

print(Tahmid+Rahim)
print(Tahmid/Rahim)

print(repr(Tahmid))
print(str(Tahmid))
