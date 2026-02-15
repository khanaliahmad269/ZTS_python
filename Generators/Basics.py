# def serve_order():
#     yield "cup1 : mocha"
#     yield "cup2: espresso"
#     yield "cup3: double"

# stall = serve_order()

# for cup in stall:
#     print(cup)


def get_coffee_list():
    return ["cup1","cup2","cup3"]

#generator function

def get_coffee_gen():
    yield "cup1"
    yield "cup2"
    yield "cup3"

coffee= get_coffee_gen()
print(coffee)
print(next(coffee))
print(next(coffee))
print(next(coffee))
print(next(coffee))