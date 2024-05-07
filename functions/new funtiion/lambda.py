# now we using the lambda funtion 
x = lambda a : a + 10
print(x(3))

# here we passing the multiple argruents 
# adding two numnber with the lambda funtion 
x = lambda a ,b : a + b  
print(x(10,20))


print("______________________________")
# anthor example 

y = lambda a , b : a + b  
print(y(4,3))

print("______________________________")
print()

# Multiple argurents passing and returning it 
z = lambda a , b , c : a * b  * c 
print(z(3,4,5))
print("_______________________________")
print()


# now we using the lambda futnion 
def my_func(n) : 
     return lambda a : a * n
Mydouble= my_func(2)
print(Mydouble(1))

print("_________________________________")

# another example
def my_func(n):
     return lambda a : a * n 
my_double  = my_func(2)
my_tripler = my_func(3)

print(my_double(11))
print(my_tripler(11))

print("_________________________________")

# here we sloving the a basic lambada futnion 
product  = lambda x , y , z  : x*y*z
print(product(x = 3,y=4,z=1))