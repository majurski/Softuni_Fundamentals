import re
number = int(input())

plant_rarity = {}
plant_rating = {}
plant_avr_rating = {}

for plants in range(number):
    line = input()
    new_line = line.split("<->")
    plant = new_line[0]
    rarity = new_line[1]

    plant_rarity[plant] = rarity


line = input()
while line != "Exhibition":

    res = re.split(': |-', line)

    command = res[0]


    if command == "Rate":
        mid_name = res[1]
        plant_name = mid_name[:-1]
        rating = float(res[2])
        if plant_name not in plant_rating:
            plant_rating[plant_name] = []
        plant_rating[plant_name].append(rating)
        avr_rating = sum(plant_rating[plant_name]) / len(plant_rating[plant_name])
        plant_avr_rating[plant_name] = avr_rating

    elif command == "Update":
        mid_name = res[1]
        plant_name = mid_name[:-1]
        new_rarity = res[2]
        plant_rarity[plant_name] = new_rarity

    elif command == "Reset":
        plant_name = res[1]
        plant_rating[plant_name] = 0.00
        plant_avr_rating[plant_name] = 0.00

    else:
        print("error")


    line = input()

plant_rarity = dict(sorted(plant_rarity.items(), key= lambda x: (-len(x[1]), x[0])))


print(f"Plants for the exhibition:")

for k,v in plant_rarity.items():
    print(f"- {k}; Rarity: {v}; Rating: {plant_avr_rating[k]:.2f}")


