lines = input().split("|")
energy = 100
coins = 100
is_bankrupt = True

for line in lines:
    new_list = line.split("-")
    event_type = new_list[0]
    event_number = int(new_list[1])

    if event_type == "rest":
        gain_energy = 0
        temp_energy = energy + event_number
        if temp_energy < 100:
            gain_energy = event_number
            energy += event_number
        else:
            gain_energy = 100 - energy
            energy = 100
        print(f"You gained {gain_energy} energy.")
        print(f"Current energy: {energy}.")

    elif event_type == "order":
        if energy < 30:
            energy += 50
            print(f"You had to rest!")
            continue
        coins += event_number
        energy -= 30
        print(f"You earned {event_number} coins.")
    else:
        if coins <= event_number:
            print(f"Closed! Cannot afford {event_type}.")
            is_bankrupt = False
            break

        coins -= event_number
        print(f"You bought {event_type}.")

if is_bankrupt:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")