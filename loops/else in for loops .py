# now we using the else statements in the for loops 
for i in range(10):
  print(i)
else: print("finally finished")

print("__________________________")

# not excuting the else executed
for i in range(6):
  if i==3: break
  print(i)
else: print("finally finished!")
print("__________________________")

# here now we using the nested loops as shown in the given below 
adj = ["red","big","tasty"]
fruits =["apple","banana","cherray"]  # ( nested loops )

for i in adj :
  for j in fruits:
    print(i,j)

print("____________________________")

# here using the pass stements 
for x in [0,1,2,3,4,5]:
  pass
