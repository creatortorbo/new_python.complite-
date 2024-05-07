# foramtting in pythons (f string )
letter = "hey my name is {1} and I am from {0}" # werare we use indexing on thies 0 and 1
country = "India "
name = "bablu"

# print(letter.format(name,country))
                  # 0      1
print(letter.format(country,name))
# here f string is f variable can use in string (using f string )
print(f"hey my name is {name} and I am from {country}")



# here we in floting value we whant 2 values in decimal
txt = "for only {price:.2f} dollars!"
print(txt.format(price = 49.09999))


# the above thing is written in (f string )
price = 49.09999
txt= f"for only {price :.2f} dollars"
print(txt)


# string calutions 
print(f"{2 * 30 }")
print(type(f"{2 * 30 }")) # checking which type is 

# only print f string (print the txt blew )
print(f" we use f-strings like this : hey my name is {{name}} and I am from {{country}}")

print("_________________________________________________________________________________")
# now we writting the f string in the given below


