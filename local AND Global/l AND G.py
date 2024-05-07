# x = 4
# print(x)

# def bablu():
#     x = 5
#     print(f"The local x is {x}")
#     print("hello bablu")

# print(f"The global x is {x}")
# bablu()
# x = 5
# print(f"The global x is {x}")


# the another example 
x = 10  # global variable 
def my_function():
    global x # here we are creted global variable (from this we can update)
    x = 4
    y = 5 # local variable 
    print(y)

my_function()
print(x)
# print(y) # this will cause an error because y is a local variable and is not accessible 
         # outside od the funtion

   