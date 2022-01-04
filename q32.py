amt=0
bill_unit=int(input("Enter number of electric unit"))
if bill_unit<=100:
     amt=0
if bill_unit>100 and bill_unit<=200:
     amt=(bill_unit-100)*5
if bill_unit>200:
     amt=500+(bill_unit-200)*10
print("Amount to pay :",amt)


    