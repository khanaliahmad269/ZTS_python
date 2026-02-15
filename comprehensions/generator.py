daily_sales = [5,10,12,3,7,8,90]

total_cups =sum((sale for sale in daily_sales if sale>2))

print(total_cups)