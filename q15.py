side1=int(input("enter the side "))
side2=int(input("enter the side1 "))
side3=int(input("enter the side2 "))
if side1+side2>=side3 and side2+side3>=side1 and side3+side1>=side2:
    print("triangle is valid ")
else:
    print("triangle is not valid ")