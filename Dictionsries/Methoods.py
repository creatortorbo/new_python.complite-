# methods of dic 

# methods 1 : update 
#data base epId : performation 
ep1 = {122:45,123:89,567:89,678:90}
ep2 = {333:90,566:90}
ep1.update(ep2)
print(ep1)

#  methods 2 : Clear()
ep1 = {122:45,123:89,567:89,678:90}
ep2 = {333:90,566:90}
ep1.clear()# clear the dic it become the dic null
print(ep1)

# we can print the empthy dic 
empt = {}
print(empt)

#  methods 2 :pop 
ep1 = {122:45,123:89,567:89,678:90}
ep1.pop(122) # here we are delating key:value both
print(ep1)

#  methods 3 :popitem()

ep1 = {122:45,123:89,567:89,678:90}
ep1.popitem() # here we are delating the last value of ep1 
print(ep1)
 

#  methods 4 :del
ep1 = {122:45,123:89,567:89,678:90} # it gives error 
# del ep1 (we ignor )
del ep1[122]
# here we are delating all the dictionary 
print(ep1)



