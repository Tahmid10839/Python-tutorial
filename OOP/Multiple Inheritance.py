
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

class Player:
    no_of_games=4
    def __init__(self,name,game):
        self.name = name
        self.game = game

    def printplayer(self):
        return f"Name: {self.name} \nGame: {self.game}"

class CoolProg(Employee,Player):
    def printcool(self):
        return f"This is a cool programmer"


Tahmid = Employee("Tahmid",10000)
Rahim = Employee("Rahim",20000)
Karim = Employee.from_str("Karim-150000")

Abar = CoolProg("Abar",60000)

print(Abar.details())



