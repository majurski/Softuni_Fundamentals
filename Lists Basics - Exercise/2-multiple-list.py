num1 = int(input())
num2 = int(input())

ls = []

for i in range(1, num2 + 1):
    multi = num1 * i
    ls.append(multi)

print(ls)