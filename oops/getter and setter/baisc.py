# here using the inhertance in the pythons 
class Employee:
   def __init__(self,name,id,life) :
      self.name = name
      self.id = id 
      self.life  = life
           

   def showdata(Self):
           print(f"The name of employee is {Self.name} and his id is {Self.id} and the  life is {Self.life}")


class programmer (Employee):
       def showLanguge(self):
            print("The default langauge is pythons")

e1 = Employee("bablu","22 -cse-4952","bad")
e1.showdata()     
# e2 = Employee("vishal","22 -cse- 4989","good ")
e2 = programmer("vishal","22 -cse- 4989","good ")

# e2.showdata()
e2.showLanguge()
      
print("_______________________________________________________________________________________________________________________________")
class Employee:
   def __init__(self,name,id,life) :
      self.name = name
      self.id = id 
      self.life  = life
           

   def showdata(Self):
           print(f"The name of employee is {Self.name} and his id is {Self.id} and the  life is {Self.life}")


class programmer (Employee):
       def showLanguge(slef):
            print("The default langauge is pythons")

e1 = Employee("bablu","22 -cse-4952","bad")
e1.showdata()
# e2 = Employee("vishal","22 -cse- 4989","good ")
e2 = programmer("vishal","22 -cse- 4989","good ")

# e2.showdata()
e2.showLanguge()

print("_______________________________________________________________________________________________________________")


