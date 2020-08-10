line = input().split("#")
water_amount = int(input())
total_fire = 0
effort = 0
is_valid = False

print(f"Cells:")
for fire in line:
    fire = fire.split(" = ")
    value_of_cell = fire[1]
    type = fire[0]

    if type == "High" and 81 < int(value_of_cell) < 125:
        is_valid = True
    if type == "Medium" and 51 < int(value_of_cell) < 81:
        is_valid = True
    if type == "Low" and 1 < int(value_of_cell) < 50:
        is_valid = True

    if is_valid and water_amount > total_fire:
        water_amount -= int(value_of_cell)
        effort += int(value_of_cell) * 0.25
        print(f" - {value_of_cell}")
        total_fire += int(value_of_cell)


print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")