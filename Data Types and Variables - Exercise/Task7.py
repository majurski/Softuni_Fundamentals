n = int(input())
capacity = 255
amount = 0

for i in range(n):
    liters = int(input())
    if capacity >= liters:
        capacity -= liters
        amount += liters
    elif capacity < liters:
        print(f"Insufficient capacity!")

print(amount)




