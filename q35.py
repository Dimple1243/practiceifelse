tax = 0
cost_price=int(input("Enter the price of bike"))
if cost_price > 100000:
     tax = 15/100*cost_price
elif cost_price >50000 and cost_price<=100000:
     tax = 10/100*cost_price
else:
     tax = 5/100*cost_price
print("Tax to be paid ",tax)
