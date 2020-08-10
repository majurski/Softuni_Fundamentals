str = input()

values = str.split()
new_values = []
for i in values:
    i =  int(i) * (-1)
    new_values.append(i)

print(new_values)

