# def fac_recursive(n):
#     if n==1:
#         return 1
#     else:
#       return n * fac_recursive(n-1)
# def fac_iterative(n):
#     fac=1
#     for i in range(n):
#        fac= fac * (i+1)
#     return fac
# user=int(input("enter the number"))
# print("The factorial of fac_recursive is",fac_recursive(user))
# print("The factorial of fac_recursive is",fac_iterative(user))
# *****fibonacci prblm*****
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
      return fibonacci(n-1)+fibonacci(n-2)
user= int(input("enter ur number"))

print(fibonacci(user))
