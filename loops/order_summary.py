'''5) You're preparing an order summary with customer names and their total bill



Tasks:

.Use two lists: one for the names and the other for their respective bill

. print"[name] paid Rs[amount]"

'''

names = ["Ali", "Aftab", "Ayesha","Khadijah", "Ahmad"]
bill =[300,250,500,750,1000]

for name,amt in zip(names,bill):
    print(f"{name} paid RS{amt}")
    