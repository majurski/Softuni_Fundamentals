items = input()

products_prices = {}
products_quantities = {}

while items != "buy":
    prods = items.split()
    name = prods[0]
    price = float(prods[1])
    quantity = int(prods[2])


    if name not in products_quantities:
        products_quantities[name] = 0

    products_prices[name] = price
    products_quantities[name] += quantity

    items = input()

for k in products_quantities.keys():
    res = products_prices[k] * products_quantities[k]
    print(f"{k} -> {res:.2f}")
