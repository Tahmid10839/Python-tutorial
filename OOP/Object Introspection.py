class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def details(self):
        return f"This Employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname ==None:
            return "Email is not set.Please set the email "

        return f"Email: {self.fname}.{self.lname} @gmail.com"

    @email.setter
    def email(self,str):
        print("Setting now....")
        names = str.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

Tahmid = Employee("Nazre Imam","Tahmid")

print(type(Tahmid))
print(id(Tahmid))
print(dir(Tahmid))
print(dir("This is"))

import inspect
print(inspect.getmembers(Tahmid))