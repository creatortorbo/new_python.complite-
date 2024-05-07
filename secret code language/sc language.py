# write a python program to translate a message into secret code language.use the rules below 
# to translate normal English into secret code language 


# coding :
# if the word contains atleat 3 charactoers , remove the first letter and append it at the end 
# now append three random characters at the starting and the end 
#else  :
# simply reverse the string 


# Decoding :
# if the word contains less than 3 characters ,reverse it 
# else :
# remove 3 random characters form start and end . Now remove the last letter and append it to 
# the beginning 
st = input("Enter message ")
words = st.split("  ")
coding = True
# coding = False
if(coding ):
    nwords = []
    for word in words :
      if(len(word)>=3):
         r1 = "fdt"
         r2 = "jld"
         stnew = r1+ word[1:] + word[0] + r2
         nwords.append(stnew)
    else:
     nwords.append(word[::-1])
    print(" ".join(nwords))

else:
   nwords = []
for word in words :
      if(len(word)>=3):
         r1 = "fdt"
         r2 = "jld"
         stnew =  word[3:-3] 
         stnew = stnew [-1] + stnew[:-1]
         nwords.append(stnew)
else:
      nwords.append(word[::-1])
      print(" ".join(nwords))
