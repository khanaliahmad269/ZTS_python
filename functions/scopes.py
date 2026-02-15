def serve_coffee():
    coffee_type = "mocha" #enclosing 
    
    def order():
        coffee_type= "espresso" #local scope
        print("inner:", coffee_type)
    order()
    print("outer:", coffee_type)

coffee_type = "cappucino" #global scope

serve_coffee()
print("global:", coffee_type)


