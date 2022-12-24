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

                 
harry=Employee("harry",255,"programmer")
rohan= Employee("ROHAN",455,"TESTER")
harry.changeleaves(25)
# print(harry.no_of_leaves)
print(Employee.no_of_leaves)
# print(harry.name)
# print(harry.printdetails())
# # print(rohan.printdetails())
# print(harry.no_of_leaves)

