import re

pattern = r"[0-9]+"


while True:

    text = input()

    if text == "":
        break

    res = re.findall(pattern, text)

    for i in res:
        print(i, end = " ")