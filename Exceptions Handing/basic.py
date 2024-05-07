# Here we are handing error (we are print the error)
a = input("Enter the number :")
print("Multiipcations table of {a} is : ")
try:
   for i in range (1,11):
    print(f"{int(a)} x {i} = {int(a)*i} ")
except Exception as e : # here print(e) is error in given 
#         print(e)  # print the error of insted of any syntax problame 
  print("Invalid Input!")                     
print("some imp lines of code ")
print("End of program")



# Spacies type of error in pyhons 
try:
  num = int(input("Enter an integer :"))
a = [6,3]
print(a[num])
exceptValueError:
         print
  