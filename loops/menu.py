'''4) You are creating a menu board.Each item must be numbered



Tasks:

. use enumerate() to print the items with numbers

'''

menu = ["Latte", "esperesso","double essperesso", "mocha", "Long Black"]

for idx, item in enumerate(menu,start=1):
    print(f"{idx}:{item}")
    