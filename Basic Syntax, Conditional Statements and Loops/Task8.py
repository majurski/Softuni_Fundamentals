str1 = input()
str2 = input()
counter = 0

cash = list(str1)
cont = []

for i in range(len(str1)):
    cash[i] = str2[i]
    new = ''.join(cash)
    if new not in cont and new != str1:
        cont.append(new)

for i in cont:
    print(i)



