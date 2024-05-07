# now we using the Arbitary keyword Arguments 
#  qnumber of keyword arguents is unknown, then add,double ** before the parameter name
def my_function(**kid):
    print("His last name is " + kid["lname"])
    print("His last name is " + kid["fname"])
my_function(fname="Tobias",lname="Refsnes")
#-------------------------------------------------------
print("______________________________________")
print()
# now another example 
def Arbitary(**name):
      print("my name is " + name["Sname"])
      print("my name is " + name["fname"])

Arbitary(fname = "bablu",Sname ="vishal")

print("______________________________________")
print()
# --------------------------------------------------------
# now Defalult parameter value
def my_function(country = "Norway"):
     print("I am from " + country)

my_function("India")
my_function("sweden")
my_function()
my_function("Brazil")

print("_________________________________________")
print()


# here passing the list as an Argument
def my_function(food):
     for i in food:
          print(i)
fruits  = ["apple","banana","cherry"]
my_function(fruits)

print("_________________________________________")
print()
# another example 
def another_example(students):
     for i in students:
          print(i)
students_name=["Bablu","Aman","Vishal","op","sumit","Deepak","Amit"]
another_example(students_name)

print("__________________________________")