# def coffee_mug(mug):
#     return mug*10

# print(coffee_mug(2))


total_coffee =12
def impure_coffee(mug):
    global total_coffee
    total_coffee += mug
    
impure_coffee(2)
print(total_coffee)