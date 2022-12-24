def funargs(list,*args):
    print(list)
    # print(type(args))
    for item in args:
        print(item)

#   print(args[0])

a=["safa","harry","nikki"]
list="the student list is"
funargs(list,*a)