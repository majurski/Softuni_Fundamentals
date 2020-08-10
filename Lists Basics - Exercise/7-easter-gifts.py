gifts = input().split(" ")
line = input()

while line != "No Money":
    token = line.split(" ")
    action = token[0]
    type = token[1]
    if action == "OutOfStock":
        count = 0
        for i in gifts:
            count += 1
            if i == type:
                gifts[count - 1] = None
    if action == "JustInCase":
        mid = ''.join(type)
        gifts[-1] = mid
    if action == "Required":
        help_index = int(token[2])
        gifts[help_index] = type


    line = input()

last_cont = []
for i in gifts:
    if i == None:
        continue
    else:
        last_cont.append(i)

for b in last_cont:
    print(b, end = " ")