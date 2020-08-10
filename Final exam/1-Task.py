text = input()

destinations = input()
while destinations != "Travel":

    all_dest = destinations.split(":")
    command = all_dest[0]

    if command == "Add Stop":
        index = int(all_dest[1])
        inserted_string = all_dest[2]
        if index > len(text):
            break
        if index >= 0 or index <= len(text)-1:
            text = text[:index] + inserted_string + text[index:]

        print(text)
    elif command == "Remove Stop":
        start_index = int(all_dest[1])
        end_index = int(all_dest[2])
        if len(text) < 0:
            break
        if start_index >= 0 and start_index <= len(text) or end_index >= start_index or end_index <= len(text):
            substring = text[start_index:end_index + 1]
            text = text.replace(substring, "")
        print(text)
    elif command == "Switch":
        old_str = all_dest[1]
        new_str = all_dest[2]

        if old_str in text:
            text = text.replace(old_str, new_str)
        print(text)
    else:
        break

    destinations = input()

print(f"Ready for world tour! Planned stops: {text}")