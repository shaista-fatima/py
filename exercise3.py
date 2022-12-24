class Electronic_device:
    fridge=52
    ac=30
    def available(self):
        return f"welcome to our gada electronic shops,available fridges are {self.fridge} and avaiable ac are{self.ac}"
class pocket_gadget(Electronic_device):
    a="anywhere door"
    b="helicopter"
    def in_my_pocket(self):
        return f"hello frds i have 2 magical things in my pocket which are {self.a} and {self.b}"
class phone(pocket_gadget):
    app="hungama"
    # b="kuch bhi"
    def my_magical_mbl(self):
        return f" hello dosto all this are available in my mbl i can watch and buy from {self.app} "

e=Electronic_device()
p=pocket_gadget()
ph=phone()
print(ph.in_my_pocket())
print(ph.b)