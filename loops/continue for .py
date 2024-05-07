# now using the continue statement 
name = ["Bablu","Vishal","Aman","Deepack","2","5","40"]
for i in name:
    if i=="Aman":
        continue  # here in the continue it skip the Aman 
    print(i)

# another example
name = ["Bablu","Vishal","Aman","Deepack","2","5","40"]
for i in name:
    if i=="Aman":
        continue  # here in the continue it skip the Aman
    if i=="5":
        continue
    
    print(i)


