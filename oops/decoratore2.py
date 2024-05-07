
# now using the basic of the decorators in the pythons as show in the  given below 
def decor(func):
   def inner():   # existing functtionlity 
      func()
      # add new uunctionality
      print("Welcome !!!!")
   return inner


def printer():
   print("welcome bablu !!")
   print("welcome bablu !!")

printer  = decor(printer) # here indited of this we use 
printer()

print("______________________________________________________________________________________________________________________")
# here it the another method of the decorators as shown in the given below 

def decor(func):
   def inner():   # existing functtionlity 
      func()
      # add new uunctionality
      print("Welcome !!!!")
   return inner

@decor   # here it used for the modefieding the funtion 
def printer():
   print("welcome bablu !!")
   print("welcome bablu !!")

# printer  = decor(printer) # here indited of this we use 
printer()


print("_________________________________________________________________________________________________________________")

# now we add thingh in fist and last  docoratore  
def vishal(func):
   def inner():
   #   print("My name is vishal")
       func()
       print("my name is Aman !!!!!")
       print("my name is Aman !!!!!")
       print("my name is Aman !!!!!")
   return inner
@vishal
def bablu():
   print("My name is bablu !")
   print("My name is bablu !!")
   print("My name is bablu !!!")

bablu()

print("________________________________________________________________________________________________________________")
