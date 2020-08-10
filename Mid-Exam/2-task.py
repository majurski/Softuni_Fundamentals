arr = input().split()
new_arr = list(map(int, arr))
result = []
line = input()

while line != "end":
    value = line.split()
    command = value[0]

    if command == "swap":
        index_1 = int(value[1])
        index_2 = int(value[2])
        new_arr[index_1], new_arr[index_2] = new_arr[index_2], new_arr[index_1]

    elif command == "multiply":
        index_1 = int(value[1])
        index_2 = int(value[2])
        multiplied = new_arr[index_1] * new_arr[index_2]
        new_arr[index_1] = multiplied

    elif command == "decrease":
        for val in new_arr:
            val -= 1
            result.append(val)

    line = input()

print(", ".join(list(map(str, result))))
# print(', '.join([str(x) for x in last]))
