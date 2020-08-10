line = input()

stores_dict = dict()

while line != "END":

    data = line.split("->")
    command = data[0]
    store = data[1]
    new_data = data[2:]

    if command == "Add":
        if store not in stores_dict:
            stores_dict[store] = []
            for i in new_data:
                stores_dict[store] = i.split(",")

        else:
            for i in new_data:
                stores_dict[store] = i.split(",")
            for i in new_data:
                stores_dict[store].append(i)


    if command == "Remove":
        if store in stores_dict:
            del stores_dict[store]

    line = input()

print("Stores list:")

stores_dict = dict(sorted(stores_dict.items(), key= lambda x: -len(x[1])))

for k, v in stores_dict.items():
    print(f"{k}")
    for i in v:
        print(f"<<{i}>>")