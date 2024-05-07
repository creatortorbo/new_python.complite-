# An objects vriables should not always be directly accessible 
# the method can ensure the correct values are set.if an incorrect values is set,the method can return an error 
# now we using the basic of the getter and the setter  as shwon in the given below 




print("_______________________________________________________________________________________________________________")

def myclass():
  def setName(self,name):
    self.name  = name 

@property
def getterName(self):
      print(f"The name is {self.name}")
    # print("helow my name is ",self.name)

obj1= myclass()
obj2= myclass()
obj1.setName("bablu")
obj2.setName("bablu")
obj1.getterName()
obj2.getterName() 

print("_____________________________________________________________________________________________________________________")
print()
# here using the getter and setter 
