# who to convert tuple into list 
countries = ("spain","Italy","India","England","Germany")
temp = list(countries)
temp.append("Rissia")  # add item 
temp.pop(3)             # remove item 
temp[2] = "finland"     # change item
countries = tuple (temp)
print(countries)