# here using the Decorating function with argruments
def my_decor(func):
    def inner (*args,**kwargs):
        print("something is happening before the function is called.")
        func(*args,**kwargs)
        print("something  is happening after the function is called.")
    return inner
@my_decor
def greet(name): 
    print(f"hello {name} !!")

greet("bablu")


print("________________________________________________________________________________________________________________")
def my_decor(func):
    def Notgood(*args,**kwargs):
           print("my life is not good")
           func(*args,**kwargs)
           print("But i am coder ")
           print("hello coder")
    return Notgood 
@my_decor
def my_lifeStyle(goodORbad):
    print(f"Life is {goodORbad}")


my_lifeStyle("Good")


