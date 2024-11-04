class employee:
    def __init__(self,eName):
        self.eName=eName

    def printemployee(self):
        print(f'eName={self.eName}')

class eInformation(employee):
    def __init__(self,eName,eNo):
        super().__init__(eNo)
        self.eNo=eNo
    def printempInformation(self):
        print(f'empaNo={self.eNo}')

class empSalary(employee):
    def __init__(self,eName,salary):
        super().__init__(eName)
        self.salary=salary
    def printempSalary(self):
        print(f'salary={self.salary}')

e=employee('vipin')
ei=eInformation('vipin',20)
es=empSalary('vipin',45000)

e.printemployee()
ei.printempInformation()
es.printempSalary()
    
    