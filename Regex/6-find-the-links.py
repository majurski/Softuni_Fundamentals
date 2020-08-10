import re

pattern = r"(www.){1}([a-zA-Z0-9\-])+((\.)([a-zA-Z]+))+"


while True:

    text = input()

    if text == "":
        break

    res = re.finditer(pattern, text)

    for mail in res:
        print(mail[0])