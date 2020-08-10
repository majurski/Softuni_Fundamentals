budget = float(input())
flour_price = float(input())
egg_price = flour_price * 0.75
milk_price = (flour_price * 1.25) / 4
countOfCozonacs = 0
coloredEggs = 0

price_of_cozonac = flour_price + egg_price + milk_price
while budget >= price_of_cozonac:
    countOfCozonacs += 1
    coloredEggs += 3
    if countOfCozonacs % 3 == 0:
        coloredEggs -= countOfCozonacs - 2
    budget -= price_of_cozonac

print(f"You made {countOfCozonacs} cozonacs! Now you have {coloredEggs} eggs and {budget:.2f}BGN left.")