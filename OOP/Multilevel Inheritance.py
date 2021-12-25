class Dad:
    basketball=1

class Son(Dad):
    dance =1
    def isdance(self):
        return f"Yes I dance {self.dance} no of time"


class Grandson(Son):
    dance = 6
    def isdance(self):
        return f"Yeah I dance awesomely {self.dance} no of time"

Tahmid = Dad()
Rahim = Son()
Karim = Grandson()
print(Karim.basketball)


#----------Exercise---------

class ElectronicDevice:
    company = "Apple"

    def iscompany(self):
        return f"Company: {self.company}"


class PocketGadget(ElectronicDevice):
    size = 6
    def issize(self):
        return f"Size: {self.size}"
class Phone(PocketGadget):
    type = "Android"
    def istype(self):
        return f"Type: {self.type}"

Electronic = ElectronicDevice()
Pocket = PocketGadget()
Mobile = Phone()
print(f"{Mobile.iscompany()} \n{Mobile.issize()} \n{Mobile.istype()}")
