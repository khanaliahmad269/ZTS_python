def update_order():
    coffee= "mocha"
    def kitchen():
        nonlocal coffee
        coffee = "espresso"
    kitchen()
    print(coffee)

update_order()
