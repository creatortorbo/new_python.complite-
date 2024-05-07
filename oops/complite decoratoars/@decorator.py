#  here we using the @  symbole for the decorators 
def my_decor(func):
     def inner():
          print("my name is vishal")
          print("And my best friend is bablu")
          func()
          print("We study in the brcm ")
     return inner
@my_decor
def say_hello():
     print("hello I am from india")

say_hello()

