line = input()
animals_food = dict()
animals_area = dict()
# areas = []
while True:
    if line == "Last Info":
        break
    else:
        new_info = line.split(":")
        process = new_info[0]
        animal_name = new_info[1]

        if process == "Add":
            animal_food_limit = new_info[2]
            animal_area = new_info[3]

            if animal_name not in animals_food:
                animals_food[animal_name] = int(animal_food_limit)
            else:
                animals_food[animal_name] += int(animal_food_limit)

            if animal_area not in animals_area:
                animals_area[animal_area] = []

            if animal_name not in animals_area[animal_area]:
                animals_area[animal_area].append(animal_name)


        elif process == "Feed":
            animal_feed = int(new_info[2])
            animal_area = new_info[3]

            if animal_name not in animals_food:
                pass

            if animal_name in animals_food:
                animals_food[animal_name] -= int(animal_feed)

            if animal_name in animals_food:
                if animals_food[animal_name] <= 0:
                    print(f"{animal_name} was successfully fed")
                    del animals_food[animal_name]

                    if animal_area in animals_area:
                        animals_area[animal_area].remove(animal_name)


        line = input()

print(f"Animals:")

animals_food = dict(sorted(animals_food.items(), key = lambda x: x[0], reverse=True))

for k, v in animals_food.items():
    print(f"{k} -> {v}g")

print(f"Areas with hungry animals:")

for k, v in animals_area.items():
    number = len(v)
    if number == 0:
        continue
    print(f"{k} : {number}")

# print(animals_area)