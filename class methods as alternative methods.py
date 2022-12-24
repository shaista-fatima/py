class Employee:
    no_of_leaves=8
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
        
    def printdetails(self):
        return f"name is {self.name}.salary is {self.salary}.role is {self.role}"
    @classmethod
    def changeleaves(cls,newleaves):
        cls.no_of_leaves=newleaves
    @classmethod
    def from_dash(cls,string):
    #   params=string.split("-")
    #   return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))
                 
harry=Employee("harry",255,"programmer")
rohan= Employee("ROHAN",455,"TESTER")
karan=Employee.from_dash("karan-250-coder")
harry.changeleaves(25)
print(karan.printdetails)
print(karan.salary)
