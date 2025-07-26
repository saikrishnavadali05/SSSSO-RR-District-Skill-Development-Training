x="global"
print(x)
#function defination
def outer():
    x="enclosing"
    print(x)

    def inner():
        x="local"
        print(x)

    inner()
outer()         