# marks = [3,4,5,6,"bablu",True]
# print(marks)
# print(marks[1:-1])
# print(marks[1:4])
# print(marks[1:4:2])


# list comprehensions 
list = [i for i in range(4)]
print(list) # in thies list we have range values 
list = [i*i for i in range(4)]
print(list)
# we can use if conditions 
list = [i for i in range(4) if i%2==0]# even no 
print(list)
list = [i for i in range(4) if i%2!=0] # odd no 
print(list)