n=int(input("enter the number "))
if n>=80:
    print("Grade A")
elif n<=80 and n>=60:
    print("Grade B")
elif n<=60 and n>=50:
    print("Grade C")
elif n>=45 and n<=50:
    print("Grade D")
elif n>=25 and n<=45:
    print("Grade E")
else:
    print("Grade F")