actual_cost=float(input("enter the cost price"))
selling_amount=float(input("enter the selling price"))
if selling_amount>actual_cost:
    print("there is a profit of " , selling_amount-actual_cost)
else:
    print("ohh you got a loss of " , actual_cost-selling_amount)