password = input()

cmd_input = input()

while cmd_input != "Done":

    comm = cmd_input.split()

    command = comm[0]

    if command == "TakeOdd":
        new_pass = ""
        for i in range(len(password)):
            if i % 2 != 0:
                if i < len(password):
                    new_pass += password[i]
        password = new_pass
        print(password)

    elif command == "Cut":
        start_index = int(comm[1])
        end_index = int(comm[2])
        if len(password) < 0:
            break
        substring = password[start_index:start_index + 3]
        password = password.replace(substring, "")
        print(password)

    elif command == "Substitute":
        symbol_1 = comm[1]
        symbol_2 = comm[2]
        if len(password) < 0:
            break
        if symbol_1 in password:
            password = password.replace(symbol_1, symbol_2)
            print(password)
        else:
            print(f"Nothing to replace!")


    cmd_input = input()

print(f"Your password is: {password}")
