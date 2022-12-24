# '''multiline comment'''
# #sinle line comment
# # a=12
# # b="hllo"
# # c=20.3
# # print(type(a))
# # print(int(c))
# a="safa how are uh"
# # print(a[0:3])
# print(a[:-1])
# print(a.endswith("uh"))
# print(a.count("a"))
# print(len(a))
# print(a.capitalize())
# print(a.find("safa"))
# c=a.replace("safa","shaista")
# print(c)
# print(a.lower())
# print(a.upper())
# a="hello how are uh all good"
# print("hello\n how are uh\n\t all good i\'am shaista\\")
# list************************
# l=["safa",1,22.0]
# print(l[1:4])
# l1=[5,1,6,2,3,4]
# l1.sort()
# l1.reverse()
# l1.append(7)
# l1.insert(7,0)
# l1.pop(4)
# l1.remove(0)
# print(l1)
# ******************tuple*****************
# a=()
# print(type(a))
# a=(2,3,1,1)
# a.count(1)
# a.index(1)
# print(a)

# print(a)
# *****************dictionary*******************
# d={"key":"value","fan":"pankha","how are uh":"kaise ho","safa":{"mrng":"roti"}}
# print(d.keys())
# d.update({"kuch bhi":"anything"})
# d.get("fan")

# print(d)
# ***************sets************
# s=set()
# s.add(1)
# s.add(2)
# print(s)
# *************conditional expressions************
# age=int(input("enter ur age:"))
# if ( age>18):
#     print("yess uh can drive")
# elif (age<18):
#     print("uh can not drive")
# else:
#     print("may be")

# a=15
# if(a>5):
#   print("ais greater")
# elif(a<47):
#     print("a is smaller")
# ****************loops************
# i=0
# while i<5:
#    print(i)
#    i+=1
num=int(input("enter ur number"))
i=0
while i<11:
    print(f"{num} x {i} = {num*i} ")
    i=i+1
