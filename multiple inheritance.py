class Employee:
    var=25
    no_of_leaves=25
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    def printdetails(self):
        return f"Employee name is {self.name},salary is{self.salary},role is {self.role}"
class player:
    var=2
    no_of_games=4
    def __init__(self,name,game):
      self.name=name
      self.game=game

        
    def printdetails(self):
        return f"player name is {self.name},game is {self.game}"
class coolprogrammer(Employee,player):
    var=10
    lang="python"
    def printlang(self):
       print(self.lang)
    


safa=Employee("safa",255,"programmer")
babe=Employee("babe",325,"coder")
hey=player("hey",["cricket"])
dude=coolprogrammer("dude",254,"coder")

# safa.name="safa"
# safa.salary=255
# safa.role="programmer"
# babe.name="babe"
# babe.salary=355
# babe.role="coder"
# print(safa.printdetails())
# print(hey.printdetails())
# p=dude.printdetails()
print(dude.var)

# print(p)
