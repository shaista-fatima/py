class Employee:
    no_of_leaves=8
    pass
harry=Employee()
rohan= Employee()

harry.name="harry"
harry.salary=450000
harry.role="programmer"

rohan.name="rohan"
rohan.salary=50000
rohan.role="tester"
rohan.no_of_leaves=6
print(rohan.__dict__)
print(rohan.no_of_leaves)
print(Employee.no_of_leaves)
Employee.no_of_leaves=5
print(Employee.no_of_leaves)
print(harry.no_of_leaves)
