class person :
#  name = "bablu"
#  occ = "Developer"
 def __init__(self,n,o):    #Constructors [def __init__(self):]   # it is donedoner method 
   print("hey I am a person ") # here the Constructors allways call
                               # with by object
   self.name = n 
   self.occ = o

#  name = "bablu"
#  occ = "Developer"

 def info(self):  # here it allways want self argurament 
   print(f"{self.name } is a {self.occ}")

a = person("bablu","Developer ")
b = person("vishal","HR")
a.info()

b.info()

# print(a.name)
# print()
# print(a.occ)
# print()
# a.name = "vishal"  # Now we updating or changeing in (f string ) 
# a.occ = "HR"
# here we print above def funtions in the given 
# f string (with help of calling )

# a.info()
# print()

    


                                