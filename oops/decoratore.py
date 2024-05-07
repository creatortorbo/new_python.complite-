# def greet(fx) :
#    def mfx ():
#       print("good morning ")
#       fx()
#       print("Thanks for using this funtion")
#       return mfx 



# @greet 
# def hello ():
#    print("hello world ")

# hello()

print("_____________________________________________________________________________________________________________________________________")


# now using the basic of the decorators in the pythons as show in the  given below 
def decor(func):
   def inner():   # existing functtionlity 
      func()
      # add new uunctionality
      print("Welcome !!!!")


def printer():
   print("welcome bablu !!")
   print("welcome bablu !!")

decor(printer)


print("____________________________________________________________________________________________________________________________________________")