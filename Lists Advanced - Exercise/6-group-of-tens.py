import math
values = list(map(int,input().split(", ")))

max_value = max(values)
num_of_groups = math.ceil(max_value / 10)

for i in range(1, num_of_groups + 1):
    current_range = []

    for val in values:
        upper = i * 10
        lower = upper - 10

        if lower < val <= upper:
            current_range.append(val)

    print(f"Group of {i * 10}'s: {current_range}")
