# here we using the constructors 
class Addition :
     first = 0
     second = 0
     answer = 0

     # parameterized constructors 
     def __init__(self,f,s) :
          self.first = f
          self.second = s

     def display(self):
          print("first number = " + str(self.first))
          print("second number = " + str(self.second))
          print("Addition of two numbers  = " + str(self.answer))

     def calculate(self):
          self.answer = self.first + self.second


obj1 = Addition(1000,2000)
obj2 = Addition(10,20)
obj1.calculate()
obj2.calculate()
obj1.display()
obj2.display()

