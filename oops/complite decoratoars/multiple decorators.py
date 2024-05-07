# here we usng the multiple decorators on a single function
def decor1(func):
      def inner():
            return func().upper()
      return inner
      
def decor2(func):
      def inner():
           
            return func().split()
      return inner
def get_name():
      name = input("Enter first name :")
      sir_name = input("Enter second name :")
      full_name = name+" "+sir_name
      return full_name
get_name = decor2(decor1(get_name))
print(get_name())


print("____________________________________________________________________________________________________________")

# here we using the @ decorators in the pythons 
def decor1(func):
      def inner():
            return func().upper()
      return inner
      
def decor2(func):
      def inner():
           
            return func().split()
      return inner

@decor2
@decor1
def get_name():
      name = input("Enter first name :")
      sir_name = input("Enter second name :")
      full_name = name+" "+sir_name
      return full_name
# get_name = decor2(decor1(get_name))
print(get_name())

print("__________________________________________________________________________________________________________")

# First decorator
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

# Second decorator
def add_greeting_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return "Hello, " + result
    return wrapper

# Third decorator
def repeat_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

@repeat_decorator
@add_greeting_decorator
@uppercase_decorator
def say_hello(name):
    return "Hello, " + name

print(say_hello("Alice"))



