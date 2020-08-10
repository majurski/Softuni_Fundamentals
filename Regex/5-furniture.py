import re

line = input()

pattern = r">>([a-zA-Z]+)<<([0-9]+(\.[0-9]+)?)!([0-9]+)"

print(f"Bought furniture:")
total_money = 0

while line != "Purchase":

    match = re.fullmatch(pattern, line)

    if match is None:
        line = input()
        continue

    print(match[1])
    price = float(match[2])
    quantity = int(match[4])
    total_money += price * quantity

    line = input()

print(f"Total money spend: {total_money:.2f}")