# here we Returing values from decorated function
def my_decorator(func):
    def inner(*args,**kwargs):
        print("something is happening before the fuction is called.")
        result = func(*args,**kwargs)
        print("something is happening after the function is called.")
        return result
    return inner
@my_decorator
def add(x,y):
    return x + y 

result = add(5,10)
print(result)

print("_______________________________________________________________________________________________________________")
def my_decorator(func):
    def inner(*args,**kwargs):
        print("here we subtrating the number as show in the given below ")
        result = func(*args,**kwargs)
        print("helow")
        return result
    return inner 

@my_decorator
def sub(x,y):
    return x - y

result = sub(5,3)
print(result)

print("_________________________________________________________________________________________________________________")