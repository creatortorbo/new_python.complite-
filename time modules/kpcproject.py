# create a program capable of dispaling questions to the user like kbc 
# use list data type to store the questions and thier correct answer 
# Display the final amount the person is taking home after palying the game 

questions = [
["which language was used to create fb ?","python","french",  # here list  is also called some times array
             "javascript","php","None",4
],
[
"which language was used to create fb ?","python","french",
             "javascript","php","None",4
],
             
[
"which language was used to create fb ?","python","french",
             "javascript","php","None",4
],
[
"which language was used to create fb ?","python","french",
             "javascript","php","None",4
],
[
"which language was used to create fb ?","python","french",
             "javascript","php","None",4
],
[
"which language was used to create fb ?","python","french",
             "javascript","php","None",4
],
[
"which language was used to create fb ?","python","french",
             "javascript","php","None",4
],
[
"which language was used to create fb ?","python","french",
             "javascript","php","None",4
],
[
"which language was used to create fb ?","python","french",
             "javascript","php","None",4
],
[
"which language was used to create fb ?","python","french",
             "javascript","php","None",4
],

]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,320000]

money = 0
for i in range (0,len(questions)):
  question = questions[i]
  print(f"\n\nQuestion for.{levels[i]}")
  print(f"a.{question[1]}           b.{question[2]}  ")
  print(f"a.{question[3]}           b.{question[4]}  ")
  reply = int (input ("Enter your answer (1-4) or 0 to quit:\n"))
  if(reply == 0):
     money = levels[i-1]  # you can quit the game with 0 
     break
  if(reply == question[-1]):
     print(f"correct answer, you have won Rs. {levels[i]}")
     if (i == 4):
        money = 10000   
     elif (i==9):
        money = 320000
     elif (i==9):
        money = 10000000
   
  else :
     print("wrong answer!")
     break 
print(f"your take home money is {money}")