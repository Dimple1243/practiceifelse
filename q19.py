Basic_Salary =int( input("Enter Basic Salary :"))
if Basic_Salary<=10000:

    DA = (Basic_Salary * 80) / 100
    HRA = (Basic_Salary * 20) / 100
    print( Basic_Salary + DA + HRA)
elif Basic_Salary<=20000:
    DA=(Basic_Salary*90)/100
    HRA=(Basic_Salary*25)
    print(Basic_Salary+DA+HRA)
else:
    Basic_Salary>=20000
    DA=(Basic_Salary*95)/100
    HRA=(Basic_Salary*30)/100
    print(Basic_Salary+DA+HRA)

    



