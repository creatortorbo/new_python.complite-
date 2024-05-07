# it is  importing all the funtions in math  funtions 
import math 

result = math.sqrt(9)  # with the help of import funtions 
print(result )         # we finding the squre root of any number 



# from keyword   # specific funtions 
from math import sqrt ,pi  # we are just importing specific funtions (sqrt,pi)

result = sqrt(9) * pi
print(result)


# importing everything with (*)
from math import *
result = sqrt(9) * pi
print(result)


# here we can as keyword(also we can write as )
import math as m
result = m.sqrt(9)*m.pi
print(result)