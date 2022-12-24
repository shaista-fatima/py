# a=5
# b=6
# c=sum((a,b))
# print(c)
def func1(a,b):
    print("hello ur in function",a+b)
def func2(a,b):
    '''This is a average of 2 numbers'''
    average=(a+b)/2
    # print(average)
    return average
# func1(1,2)
# v=func2(2,4)
# print(v)
print(func2.__doc__)