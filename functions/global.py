coffee_type = "mocha"

def front_desk():
    def kitchen():
        global coffee_type
        coffee_type="espresso"
        
    kitchen()
    print(coffee_type)

front_desk()
print(coffee_type)
