def infinite_coffee():
    count = 1
    while True:
        yield f"Refil #{count}"
        count+=1

user1 = infinite_coffee()
user2 = infinite_coffee()

for _ in range(3):
    print(next(user1))


for _ in range(5):
    print(next(user2))