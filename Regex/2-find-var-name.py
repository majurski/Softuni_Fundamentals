import re

pattern = r"\b_([a-zA-Z0-9]+)\b"

text = input()

all_vars = []

res = re.findall(pattern, text)

for i in res:
    all_vars.append(i)

print(",".join(all_vars))