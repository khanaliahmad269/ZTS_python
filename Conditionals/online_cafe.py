order_amount = int(input("Enter the order amount: "))


dilevery_charges=0 if order_amount >= 1000 else 100

print(f"Yor order amount is {order_amount} and the dilivery charges are {dilevery_charges}")
