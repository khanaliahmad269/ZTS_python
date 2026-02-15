# def local_coffee():
#     yield "mocha"
#     yield "espresso"

# def imported_coffee():
#     yield "macha"
#     yield "caramel iced latte"

# def menu():
#     yield from local_coffee()
#     yield from imported_coffee()

# for coffee in menu():
#     print(coffee)

def stall():
    try:
        while True:
            order = yield "waiting for order"
    except:
        print("Stall closed, no more coffee")
    
coffee_stall = stall()
print(next(coffee_stall))

coffee_stall.close()   #clean the memory
