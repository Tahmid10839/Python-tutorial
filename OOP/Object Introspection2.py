class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{fname}.{lname}@gmail.com"
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set.Please set it using setter"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self,string):
        print("Setting now")
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None


apoorv=Employee("Apoorv","Ranjan")
import inspect
for name,data in inspect.getmembers(apoorv):
    if name.startswith('__'):
        continue
    print('{}: {!r}'.format(name,data))
for key,data in inspect.getmembers(apoorv,inspect.isclass):
    print('{}:{!r}'.format(key,data))
from pprint import pprint
pprint(inspect.getmembers(apoorv, inspect.isfunction))
print(inspect.getsource(apoorv.__init__))