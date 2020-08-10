number = int(input())

hit_points_store = {}
mana_points_store = {}


for i in range(number):
    filling = input().split()

    name = filling[0]
    hit_points = filling[1]
    mana_points = filling[2]

    hit_points_store[name] = int(hit_points)
    mana_points_store[name] = int(mana_points)

line = input()

while line != "End":

    command = line.split(" - ")
    comm = command[0]
    name = command[1]

    if comm == "CastSpell":
        mana_points_needed = int(command[2])
        spelled_name = command[3]
        if mana_points_store[name] >= mana_points_needed:
            mana_points_store[name] -= mana_points_needed
            print(f"{name} has successfully cast {spelled_name} and now has {mana_points_store[name]} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spelled_name}!")

    elif comm == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        if hit_points_store[name] > 0:
            hit_points_store[name] -= damage
            if hit_points_store[name] <= 0:
                print(f"{name} has been killed by {attacker}!")
                del hit_points_store[name]
            else:
                print(f"{name} was hit for {damage} HP by {attacker} and now has {hit_points_store[name]} HP left!")

    elif comm == "Recharge":
        increase_amount = int(command[2])
        mana_points_store[name] += increase_amount

        if mana_points_store[name] >= 200:
            print(f"{name} recharged for {mana_points_store[name] - 200} MP!")
            mana_points_store[name] = 200
        elif mana_points_store[name] < 200:
            print(f"{name} recharged for {increase_amount} MP!")

    elif comm == "Heal":
        heal = int(command[2])
        hit_points_store[name] += heal
        if hit_points_store[name] > 100:
            print(f"{name} healed for {(heal + 100) - hit_points_store[name]} HP!")
            hit_points_store[name] = 100
        elif hit_points_store[name] < 100:
            print(f"{name} healed for {heal} HP!")


    line = input()

hit_points_store = dict(sorted(hit_points_store.items(), key= lambda x: x[1], reverse=True))
mana_points_store = dict(sorted(mana_points_store.items(), key= lambda x: x[0]))


for k, v in hit_points_store.items():
    print(f"{k}")
    print(f"HP: {v}")
    print(f"MP: {mana_points_store[k]}")