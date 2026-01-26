cup = input("Enter the desired cupsize(Small/Medium/Large): ").lower()

if cup == "small":
    print(f"The price of {cup} is Rs.300")
elif cup == "medium":
    print(f"The price of {cup} is Rs.500")
elif cup =="large":
    print(f"The price of {cup} is Rs.700")
else:
    print("invalid cup size entered")