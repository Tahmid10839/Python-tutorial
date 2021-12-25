
class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalary):
        self.name = aname
        self.salary = asalary
    def details(self):
        return f"Name: {self.name} \nSalary: {self.salary} \nNo of leaves: {self.no_of_leaves}"



Tahmid = Employee("Tahmid",10000)
Rahim = Employee("Rahim",20000)

print(Tahmid.details())
print(Tahmid.salary)
print(Rahim.details())