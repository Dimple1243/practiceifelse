age=int(input("enter the age "))
sex=input("enter the sex M/F" )
day=int(input("enter the working days "))
if age >=18 and age < 30:
    if sex=='M':
     wage= day*700
     print("Total wages is : ", wage)
elif age >=18 and age < 30:
    if sex == 'F':
     wage = day*750
     print("Total wages is : ", wage)
elif age >=30 and age <= 40: 
    if sex== 'M':
     wage = day * 800
     print("Total wages is : ",wage)
elif age >=30 and age <= 40 :
    if sex == 'F':
     wage = day * 850
     print("Total wages is : ",wage)
else:
     print("Enter appropriate age")