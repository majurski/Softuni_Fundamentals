import re
line = input().split(", ")

for i in line:
    if 3 < len(i) < 16:
        if re.match("^[a-zA-Z0-9_.-]+$", i):
            print(i)

