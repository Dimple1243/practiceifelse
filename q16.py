x = int(input("lenght of the x"))
y = int(input("lenght of the y "))
z = int(input("lenght of the z "))

if x == y == z:
	print("Equilateral triangle")
elif x==y or y==z or z==x:
	print("isosceles triangle")
else:
	print("Scalene triangle")
