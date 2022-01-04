year=int(input("enter the year:"))
month=int(input("enter the month [1-12]: "))
day=int(input("next date is [yyyy-mm-dd] :"))
if month==2:
    if day>0 and day<29 and year%4==0:
        print(day+1,"-",month,"-",year)
    elif day>0 and day<28:
        print(day+1,"-",month,"-",year)
    else:
        print("enter the correct day")
elif month==1 and 3 and 5 and 7 and 8 and 10 and 12:
    if day>0 and day<31:
        print(day+1,"-",month,"-",year)
    else:
        print("enter the correct day")
elif month==4 or 6 or 9 or 11:
    if day>0 and day<30:
        print(day+1,"-",month,"-",year)
    else:
        print("enter the correct day")
else:
    print("enter the correct day")



    