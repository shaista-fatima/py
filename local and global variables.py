# l=10 #global variable
# # b=11
# def func(n):
#     # l=5 #local variable
#     # m=8
#     global l # global keyword is used to change the value of global variable
#     l=l+335
#     print(l)
#     # print(m)
#     # print(b)

#     print(n,"hey am safa")
# func("whatsapp")
# # print(l)
#***** nested functions*******
def harry():
    x=20
    def rohan():
        global x # this wont change the value of local variable
        x=50
    print("befor calling rohan()",x)
    rohan()
    print("after clling rohan",x)
harry()
# rohan()

