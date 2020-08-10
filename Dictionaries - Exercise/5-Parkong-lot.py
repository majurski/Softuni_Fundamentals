number_of_com = int(input())

parking_lot = {}

for i in range(number_of_com):
    line = input().split()
    command = line[0]
    name = line[1]

    if command == "register":
        reg_plate = line[2]

        if name in parking_lot:
            print(f"ERROR: already registered with plate number {parking_lot[name]}")
            continue

        parking_lot[name] = reg_plate
        print(f"{name} registered {parking_lot[name]} successfully")

    elif command == "unregister":
        if name not in parking_lot:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            del parking_lot[name]

for k,v in parking_lot.items():
    print(f"{k} => {v}")
