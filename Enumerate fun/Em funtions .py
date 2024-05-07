# when it is use of valriable and updtions 
# marks = [12,56,32,98,12,45,1,4]

# index =0
# for mark in marks :
#    print(mark)
#    if(index == 3):
#       print("bablu, name") 
#    index +=1 




# now we using of Enumerate funtions 
marks = [12,56,32,98,12,45,1,4]
for index , mark in enumerate(marks):
   print(mark)
   if(index == 3):
      print("bablu, name") 



# here we can change the index 
marks = [12,56,32,98,12,45,1,4]
for index , mark in enumerate(marks, start = 1):
   print(mark)
   if(index == 3):
      print("bablu, name") 
