# Set Methods

# Methods 1 : union 
s1 = {2,3,5,6}
s2 = {7,8,9,6}
print(s1.union(s2))

# Methods 2 : update 
s1 = {2,3,5,6}
s2 = {7,8,9,6}
no = s1.update(s2)
print(s1,s2)


# pritices questions (for intersection )
cities1 = {"Tokyo","Madrid","Berlinl","Delhi"}
cities2 = {"tokyo","seoul","kabul","Madrid"}
cities3 = cities1.intersection(cities2)
print(cities3)


# symmetices diff (not common )
cities1 = {"Tokyo","Madrid","Berlinl","Delhi"}
cities2 = {"tokyo","seoul","kabul","Madrid"}
cities3 = cities1.symmetric_difference(cities2)
print(cities3)
  

# A-b 
cities1 = {"Tokyo","Madrid","Berlinl","Delhi"}
cities2 = {"tokyo","seoul","kabul","Madrid"}
cities3 = cities1.difference(cities2)
print(cities3)

# Methods 3 : isdisjoint 
# In this methods it not have common element 
cities1 = {"Tokyo","Madrid1","Berlinl","Delhi"}
cities2 = {"tokyo","seoul","kabul","Madrid"}
cities3 = cities1.isdisjoint(cities2)
print(cities3)


# Methods 4 : superset (subset)

cities1 = {"Tokyo","Madrid1","Berlinl","Delhi"}
# cities2 = {"seoul","kabul"}
# print(cities1.issubset(cities2))
cities3 = {"tokyo","Delhi","Madrid1"}
print(cities1.issubset(cities3))


