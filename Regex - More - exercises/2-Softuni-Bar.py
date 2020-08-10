import re

line = input()

pattern = r"%([a-zA-Z]+)%<([a-zA-Z]+)>\|([0-9])\|([0-9]+[.][0-9])"

total = 0

while line != "end of shift":


    res = re.finditer(pattern, line)

    for mail in res:
        name = mail[1]
        product = mail[2]
        amount = int(mail[3])
        price = float(mail[4])
        temp_price = amount * price
        total += temp_price
        print(f"{name}: {product} - {temp_price:.2f}")


    line = input()

print(f"Total income: {total:.2f}")

