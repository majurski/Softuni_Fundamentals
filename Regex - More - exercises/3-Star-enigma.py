import re

number = int(input())

pattern = r"[starSTAR]"
pattern2 = r"([a-zA-Z]+)[0-9]*(@[a-zA-Z]+)*:([0-9]+)!([AD])!->([0-9]+)"

attacked_planets = 0
destroyed_planets = 0

attacked = {}
destroyed = {}

for i in range(number):
    info = input()
    res = re.findall(pattern, info)
    the_key = len(res)
    new_info = ""

    for symbol in info:
        new_info += chr(ord(symbol) - the_key)

    decode = re.finditer(pattern2, new_info)

    for planet in decode:
        planet_name = planet[1]
        planet_population = planet[3]
        attack_type = planet[4]
        soldiers_count = planet[5]

        if attack_type == "A":
            attacked_planets += 1
            attacked[planet_name] = planet_name

        if attack_type == "D":
            destroyed_planets += 1
            destroyed[planet_name] = planet_name


print(f"Attacked planets: {attacked_planets}")
attacked = dict(sorted(attacked.items(), key=lambda x: x[1]))
for k in attacked:
    print(f"-> {k}")
print(f"Destroyed planets: {destroyed_planets}")

destroyed = dict(sorted(destroyed.items(), key=lambda x: x[1]))
for k in destroyed:
    print(f"-> {k}")
