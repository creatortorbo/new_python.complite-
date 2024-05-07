# accessing multiple values (keys in )
# it is printing all the keys of dec 
info = {'name':"bablu","age" :19,'eligible' : True}
print(info)
print(info.keys ()) 
print(info.values())  # it printing values in dec 


# print dec with loops (values)
info = {'name':"bablu","age" :19,'eligible' : True}
for key in info .keys ():
  # using f string 
  print(f"The value corresponding to the key {key} is {info[key]}")

          

# keyes - vlaues pair (print keys values )
print(info.items()) 
# in loops itreating 
for key,value in info.items():
   print(f"The value corresponding to the key {key} is {value}")


