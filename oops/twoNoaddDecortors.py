# here we using the decorators in this we add the 3 number
def decor(addition):
    def inner():
       result = addition() 
       num3 = float(input("Enter third number :"))
       result = result + num3
       print("The sum of three number is ",result)
       
#        return result
    return inner 
    
@decor
def addition():
  num1 = float(input("Enter first number :"))
  num2 = float(input("Enter second number :"))
  result = num1 + num2
  print("The sum of two number : ",result)
  return result 


addition()


 
