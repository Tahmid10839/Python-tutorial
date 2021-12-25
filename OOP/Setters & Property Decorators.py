
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
Rahim = Employee("Rahim",'Rahman')

print(Tahmid.email)
Tahmid.fname = "Tahmid"
print(Tahmid.email)

Tahmid.email = "Tahmid.Hassan@gmail.com"
print(Tahmid.fname)
print(Tahmid.lname)
print(Tahmid.email)

del Tahmid.email
print(Tahmid.email)

Tahmid.email = "Tahmid.Hassan1@gmail.com"
print(Tahmid.email)