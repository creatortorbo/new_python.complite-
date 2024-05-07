class Myclass:
     def __init__(self,value) :# con
          self.__value = value
def show (self):
   print(f"value is {self.value}")    
@property # dec
def value(self):
     return self._value
obj = Myclass(10)  # Getter
print(obj._value)
obj.show()