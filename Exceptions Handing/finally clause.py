# try :
#    l = [1,5,6,7]
#    i = int(input("Enter the index :"))
#    print(l[i])
# except:
#    print("some error occurred")


# finally:
#  print("I am always executed ")  # it will always run 
#                                   # any time 
# #  print("I am always executed ")  some times it print 
# # but some it not print that way we use is (finally )



# with using in  functions (finally``)
def func1():
  try :
    l = [1,2,4,5]
    i = int(input("Enter  the index :")) 
    print(l[i])     # here in this (print ("funtions is not works "))
    return 1
  except:
    print("some error occured ")

x = func1()
print(x)