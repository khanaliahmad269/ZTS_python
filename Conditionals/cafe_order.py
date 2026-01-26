snacks = input("Give your order: ").lower()
#print(snacks)

if snacks == "cookie" or snacks=="samosa":
    print(f"Great Choice!! WE are gonna serve you {snacks}")
else:
    print(f"Sorry!! {snacks} is unavailable.")