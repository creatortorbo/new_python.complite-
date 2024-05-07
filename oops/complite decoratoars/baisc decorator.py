def my_decorator(func):
     def wrpper():
          print("something is happening before the function is called .")
          func()
          print("something is happening after the function is called.")

     return wrpper

def say_hello():
       print("hello !!")



say_hello = my_decorator(say_hello)

say_hello()

print("________________________________________________________________________________________________________________")
def my_decorator(func):
      def inner():
            
         print("my name is vishal")
         func()
         print("my name is aman")
      return inner 
    
def bablu():
      print("my name is bablu and I am from brcm ")

bablu = my_decorator(bablu)
bablu()