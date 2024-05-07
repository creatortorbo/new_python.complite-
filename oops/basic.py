# now we using the basic oops 
class studant:
     name = "bablu"
     collage = "studant"
     collageFree = "4000"

a = studant()

print("my name is ",a.name,"I am collage",a.collage,"and my collage free is ",a.collageFree)  # a.name we are printng upadating values 

print("____________________________________________________________________________________________________________")
class studant:
     name = "bablu"
     collage = "studant"
     collageFree = "4000"

a = studant()
a.name= "Vishal"  # here  here we are updating the  info
a.collage = "football player"
a.collageFree = "4900"
print(a.name,a.collage,a.collageFree)  # a.name we are printng upadating values 

print("___________________________________________________________________________________________________________")
class studant :
     name = "Aman"   
     collage = "studant"
     collageFree = "4500"
     

     def info(self):  # here usng the f string in the oops as shown in the given below 
          print(f"My is {self.name} I am collage {self.collage} and my collage free is {self.collageFree}")


a = studant()

# print(a.name,a.collage,a.collageFree)
a.info()


print("______________________________________________________________________________________________________________")
class person :  # object 
     name = "bablu"
     cocuppations = "Softwere Developer"
     networth = 18 

     def info(self):
          print(f"{self.name} is a {self.cocuppations}")
                             # self mean that is who that is calling 
a = person()
b = person()
a.name = "vishal"
b.name = "Aman"
a.cocuppations = "Accountant"
b.cocuppations = "HR"
# print(a.name,a.cocuppations)
a .info()
b.info()
print("_____________________________________________________________________________________________________________________")

# # now we tacking the another example of the oops 
class collage :
   name = "Bablu"
   RollNumber = "4952"   # here self is a parameter for accessing the varible 
   collageFee = "500000"
   def info (self):
        print(f"my name is {self.name} and my collage Roll number is {self.RollNumber} and my collagefee is {self.collageFee}")

s

a = collage ()

b = collage ()
a .name = "Aman"
a.RollNumber = "4989"
a.collageFee = "500000"
b.name = "Vishal"
b.RollNumber = "4989"
b.collageFee= "500000"

a.info()
b.info()

print("__________________________________________________________________________________________________________________")
