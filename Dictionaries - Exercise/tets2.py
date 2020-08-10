cars = {}
car_input = input().split()

while True:

    if car_input[0] == "Stop":
        break

    owner = car_input[0]
    brand = car_input[1]
    mileage = car_input[2]

    if owner not in cars:
        cars[owner] = []
        cars[owner].append({brand: mileage})
    else:
        cars[owner].append({brand: mileage})

    car_input = input().split()


for i in cars["Петко"]:
    for k,v in i.items():
        print(k, v)
