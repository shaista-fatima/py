class Employee:
    no_of_leaves=8
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
        
    def printdetails(self):
        return f" the Employee name is {self.name}.salary is {self.salary}.role is {self.role}"


class programer(Employee):
    def printprog(self): 
        return f"The programmer name is {self.name} . salary is {self.salary}.role is {self.role}"

harry=Employee("harry",255,"programmer")
rohan= Employee("ROHAN",455,"TESTER")
safa=programer("safa",265,"coder")
print(safa.printprog())
print(safa.no_of_leaves)
print(safa.printdetails())


print(harry.name)
print(harry.printdetails())
# print(rohan.printdetails())

