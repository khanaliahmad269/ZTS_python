menu =[
    "mocha",
    "Iced lemon Tea",
    "Green Tea",
    "Iced caramel Latte",
    "Americano",
    "Latte"
]

# list = [expression for item in iterable if condition]

iced_item = [iced for iced in menu if "Iced" in iced]

print(iced_item)
