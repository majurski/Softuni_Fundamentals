import re

pattern = r"(@#+)([A-Z][a-zA-Z0-9]{4,}[A-Z])(\1)"
pattern2 = r"[0-9]+"
number = int(input())

for i in range(number):

    line = input()

    result = re.fullmatch(pattern, line)

    if result == None:
        print(f"Invalid barcode")
    else:
        barcode = str(result[0])
        new_result = re.findall(pattern2, barcode)
        if len(new_result) == 0:
            print(f"Product group: 00")
        else:
            group_name = "".join(new_result)
            print(f"Product group: {group_name}")