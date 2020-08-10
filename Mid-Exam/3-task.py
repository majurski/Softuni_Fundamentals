array = input().split()
new_arr = list(map(int, array))

avr = sum(new_arr) / len(new_arr)

last = []

for i in new_arr:
    if i > avr:
        last.append(i)

last.sort(reverse = True)

if len(last) > 0:
    for i in last[:5]:
        print(i, end=" ")
else:
    print("No")
