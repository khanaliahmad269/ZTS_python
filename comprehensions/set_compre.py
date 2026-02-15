# menu =[
#     "mocha",
#     "Iced lemon Tea",
#     "Green Tea",
#     "Iced caramel Latte",
#     "Americano",
#     "Latte"
# ]

# unique_coffee = {beverage for beverage in menu if len(beverage)>10}

# print(unique_coffee)



recipes = {
    "mocha":["single shot", "chocolate", "milk", "sugar"],
    "espresso": ["single shot"],
    "machiato": ["double shot", "milk"]
}

unique_recipes ={items for ingredients in recipes.values() for items in ingredients}

print(unique_recipes)