class Employee:
    no_of_leaves = 8
    pass

Tahmid = Employee()
Rahim = Employee()

Tahmid.name = "Tahmid"
Tahmid.salary = 10000

Rahim.name = "Rahim"
Rahim.salary = 20000

print(Employee.__dict__)
print(Employee.no_of_leaves)
Rahim.no_of_leaves = 9
print(Rahim.__dict__)
print(Tahmid.no_of_leaves,"\n",Rahim.no_of_leaves)


