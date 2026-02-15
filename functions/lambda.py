coffee_types = ["mocha","esspresso","machiato","latte","Double"]

strong_coffee= list(filter(lambda coffee: coffee=="esspresso" or coffee=="Double",coffee_types))

print(strong_coffee)
