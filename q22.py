salary=int(input("enter the salary "))
service_year=int(input("enter the service year "))
if service_year>=5:
    bonus_amount=salary+(salary/5*100)
    print("bonus",bonus_amount)
else:
    print("you will not get bonus")
