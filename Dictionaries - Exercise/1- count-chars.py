from collections import defaultdict

text = input()

cont = defaultdict(int)

for i in text:
    if i != " ":
        cont[i] += 1

for k,v in cont.items():
    print(f"{k} -> {v}")
