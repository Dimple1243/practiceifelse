quanitity=int(input("enter the quantity "))
purchase_amount=int(input("enter the purchse_amount "))
total_amount=quanitity*purchase_amount
discount=total_amount*10/100
if total_amount>1000:
    print("you get discount",discount,"for shopping visit again")
else:
    print("total_amount is",total_amount,"you don't get any discount"   )
