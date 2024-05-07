# In the Constructors we using the basic if else : as requriedments 
class myclass :
      def __init__(self,name=None):
            if name is None :
                  print("Default constructor called")
            else: 
                  self.name = name 
                  print('parameterized constructor called with name',self.name)

      def method(self):
              if hasattr(self,'name'):
                  print("Method called with name",self.name)

              else:
                 print("Method called without a name ")

obj1 = myclass()
obj1.method()
obj2 = myclass("Bablu")
obj2.method()

