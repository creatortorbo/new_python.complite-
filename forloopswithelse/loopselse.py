# for i in []:
#   print(i)

# else:  # we can using else in the loops 
#   print("sorry no i")


# else not printed 
for i in range(6):
    print(i)
    if i == 4: # (here loops is break than loops complited  )
       break   # not works else conductions 
    
else :
   print("sorry no i")



# exlample 
for x in range (5):
   print("iterations no {} in for loops".format(x+1))

else:
   print ("esle block in loops")

print("out of loops ")
   