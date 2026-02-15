# coffee = [10,20,30]
# def order(mug):
#     mug[1] = 27
#     print(mug)

# order(coffee)


def prepare_coffee(milk,sugar):
    print(milk,sugar)

prepare_coffee("yes","low") #positional 

prepare_coffee(sugar="no", milk="yes") #keywords 

def special(*ingredients , **extras): # * --> args  ** --> kwargs
    print("Ingredients",ingredients)
    print("Extras",extras)

special("coffee beans","sugar", "milk", sweatner="brown sugar", foam ="yes")




