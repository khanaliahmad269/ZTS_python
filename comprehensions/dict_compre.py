coffee_prices_pkr = {
    "mocha":350,
    "espresso":250,
    "double": 400
}

coffee_prices_usd = {coffee:prices/280 for coffee,prices in coffee_prices_pkr.items()}

print(coffee_prices_usd)