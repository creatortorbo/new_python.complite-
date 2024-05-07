# constructors ----> it is made for making a objects 
# now we using the basic constructors 
class person :
      def __init__(self):
             print("hey my name is bablu")

def info(self) :
   print(f"{self.name} is a {self.acc}")

a = person()
b = person()

# a.name = "bablu"
# a.occ = "Hr"

print("__________________________________________________________________________________________________________________________")

class studants :
     def __init__(self,o,n):  # here we  have the constructors
          print(" my name is bablu") 
          self.name = o
          self.collagename = n

def info(self):
     print(f"hey my name is {self.name} and the my collage name is {self.collagename}")
   

a = studants("Bablu","BRBM collage ingg and tech")
b = studants("Aman","BRCM collage of ing and tech ")
a.info()
b.info()

print("________________________________________________________________________________________________________________________________")
class person :
   def __init__(self,n,o) :
        print("hey I am a person")
        self.name = n
        self.occ = o


def info(self):
     print(f"{self.name} is a {self.occ}")


a = person("bablu","Developer")
b = person("Aman","hr")
a.info()
b.info()