class Employee:
    no_of_leaves=8
    def printdetails(self): # methods
        # self.name=name
        # self.salary=salary
        return f"name is {self.name}.salary is {self.salary}.role is {self.role}"
harry=Employee()
rohan= Employee()

harry.name="harry"
harry.salary=450000
harry.role="programmer"

rohan.name="rohan"
rohan.salary=50000
rohan.role="tester"
rohan.no_of_leaves=6

print(harry.printdetails())
print(rohan.printdetails())

