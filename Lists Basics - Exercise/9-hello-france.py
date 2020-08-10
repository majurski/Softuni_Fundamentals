type_price = input().split("|")
budget = float(input())
profit = 0.00
newItems = []

for items in type_price:
    is_valid = True
    item = items.split("->")
    item_type = item[0]
    item_price = float(item[1])

    if item_type == "Clothes" and item_price > 50:
        is_valid = False
    if item_type == "Shoes" and item_price > 35:
        is_valid = False
    if item_type == "Accessories" and item_price > 20.50:
        is_valid = False

    if is_valid:
        budget -= item_price
        salePrice = item_price * 1.4
        profit += salePrice - item_price
        newItems.append(salePrice)

finalPrice = 0
finalList = []
for i in newItems:
    finalPrice += i
    finalList.append(str(f"{i:.2f}"))

print(' '.join(finalList))

print(f"Profit: {profit:.2f}")
if finalPrice + budget >= 150:
    print("Hello, France!")
else:
    print('Time to go.')