# here we using the continue statement 
# i = 0
# while i<6:
#   i+=1
#   if i==3:
#     continue
#   print(i)

i = 0
while i<10:
  i+=1
  if i==3:
    continue  # here uisng the continue for the skip the number 
  if i==6:
    continue
  print(i)

print("_______________________________")  # here it for the dived the code into to parts and the output 

# uisng the else in the continue statement 
i = 0
while i<10:
  i+=1
  if i==3:
    continue 
 
  print(i)
else : print("i is no less than 10")