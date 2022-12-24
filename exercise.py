mydic={"how are uh":"kaise ho aap","what is ur name":"apka naam kya hai","where r uh from":"aap kidr se ho"}
print( "options are :", mydic.keys())
user=input("enter ur word:\n")
print(mydic.get(user))