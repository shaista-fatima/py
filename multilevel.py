class dad:
    basketball=1
class son(dad):
    dance=1
    basketball=10
    def isdance(self):
     return f"i can dance disco deewane wala step {self.dance} of this times"
class grandson(son):
    dance=6
    # basketball=25
    def isdance(self):
        return f" i can dance for the song coca cole {self.dance} for this many times"

d=dad()
s=son()
g=grandson()
print(g.isdance())
print(g.basketball)





















































# class dada:
#     song="pyaar kia tho darna kya"
# class dad(dada):
#     song="kuch kuchhota hai"
# class son(dad):
#     pass
#     # song="coca cola tu"
# da=dada()
# d=dad()
# s=son()
# print(s.song)
