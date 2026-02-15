def customer():
    print("Welcome!! what coffee will you like?")
    order=yield
    while True:
        print(f"preparing {order}")
        order=yield

stall = customer()
next(stall) #generator starts
stall.send("mocha")
stall.send("green Tea")
