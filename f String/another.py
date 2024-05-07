# here using the another example of the f string as shwon in the given below 
letter = "hey my name is {} and I am from {}"
country = "India"   
name = "bablu"
print(letter.format(name,country))

print("____________________________________________________________________________________________________________________")
print()
# uisng with the index as shwon in the given 
letter = "hey my name is {1} and I am from {0}"
country = "India"   #  string 
name = "bablu"

print(letter.format(name,country))

print("__________________________________________________________________________________________________________________")  # it for the dividing the programe 

# here we using the defulit 
letter = "hey my name is {} and I am from {}"
country = "India"   #  string 
name = "bablu"

print(letter.format(country,name))    # here we changes the postion of the arrgruments in the format 

print("_________________________________________________________________________________________________________________________________________________________________________")

# here uisng the simple basic string 

letter = "hey my name is {} and I am from {} and my best frined is {} , I complited my b tech from collage {} and also I comlited my mtech from {}"
country = "India"   
name = "bablu"
friend = "om"
Btech_collage = "BRCM collage of the ingg and techonlogy"
Mtech_collage = "IIT"
print(letter.format(country,name,friend,Btech_collage,Mtech_collage))    # here we changes the postion of the arrgruments in the format 


print("________________________________________________________________________________________________________________________________________________________________________________________")

# #  now we using the f string 

country = "India"   
name = "bablu"
friend = "om"
Btech_collage = "BRCM collage of the ingg and techonlogy"
Mtech_collage = "IIT"

print(f"hey my name is {name} and I am from {country} and my best frined is {friend} , I complited my b tech from collage {Btech_collage} and also I comlited my mtech from {Mtech_collage}")
# here we using the f string 
print("______________________________________________________________________________________________________________________________________")

# here in float values seen two decimal olny give 2decimale places 
text = "for only {price: .2f} dollars!"  # it uisng for normale form 
print(text.format(price = 49.09999999))  # here it printed the two decmils in vlues 

txt = "for only {price:.3f} dollars !"
print(txt.format (price=50.0999999999))  # for 3 decmile points it can printed


txt = "for only {price:.4f} dollars !"
print(txt.format (price=50.0999999999))    # 4 decmaile points 

txt = "for only {price:.1f} dollars !"
print(txt.format (price=50.0999999999)) # 1 decmile points 

txt = "for only {price:.5f} dollars !"  # 5 decmile points 
print(txt.format (price=50.0999999999))

txt = "for only {price:.6f} dollars !"
print(txt.format (price=50.0999999999))  # 6 decmile points 

print()
# here the above code we can written form of f string 
price = 49.09999999
txt = f"for only {price:.2f} dollars !!!"
print(txt)
price = 49.09999999
txt = f"for only {price:.1f} dollars !!!"
print(txt)
price = 49.09999999
txt = f"for only {price:.3f} dollars !!!"
print(txt)
price = 49.09999999
txt = f"for only {price:.4f} dollars !!!"
print(txt)
price = 49.09999999
txt = f"for only {price:.5f} dollars !!!"
print(txt)
print("____________________________________________________________________________________________________________________________")
# here uisng in opertaion 
print(f"{2 * 30}")
print(f"{2 * 3}")
print(f"{1 * 30}")

print("____________________________________________________________________________________________________________________________")

