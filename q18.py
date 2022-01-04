Physics=int(input("Enter marks of the  Physics"))
Chemistry=int(input("Enter marks of the Chemistry "))
Biology=int(input("Enter marks of the Biology"))
Mathematics=int(input("Enter marks of the Mathematics"))
Computer=int(input("Enter marks of the Computer "))
# avg= Physics+Chemistry+Biology+Mathematics+Computer/5
Percentage=(Physics+Chemistry+Biology+Mathematics+Computer)/500*100
if Percentage>=90:
    print("Grade : A")
elif Percentage>=80: 
    print("Grade: B")
elif Percentage >= 70 : 
    print("Grade: C")
elif Percentage >= 60 : 
    print("Grade: D")
elif Percentage >= 40:
    print("Grade: E")
else:
    print('"Grade: F')