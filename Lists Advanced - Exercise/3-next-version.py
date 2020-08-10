version = input().split(".")

first = int(version[0])
second = int(version[1])
third = int(version[2])

if second == 9 and third == 9:
    first += 1
    second = 0
    third = 0

elif third < 9:
    third += 1
elif third == 9:
    third = 0
    second += 1

print(f"{first}.{second}.{third}")
