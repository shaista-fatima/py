def dec1(func1):
    def nowexec():
        print("am a function and am executing")
        func1()
        print("executed")
    return nowexec
@dec1
def hello():
    print("harry is a gud boy")

# who_is_harry = dec1(who_is_harry)
# hello = dec1(hello)
hello()
