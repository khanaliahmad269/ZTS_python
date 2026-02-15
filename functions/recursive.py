def pour_coffee(n):
    if n == 0:
        return "All cups poured"
    return pour_coffee(n-1)

print(pour_coffee(5))


