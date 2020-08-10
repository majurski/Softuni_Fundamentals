electron_number = int(input())
shell = []
shell_index = 1

while electron_number > 0:
    value = 2 * shell_index ** 2
    if electron_number < value:
        shell.append(electron_number)
    else:
        shell.append(value)
    electron_number -= value
    shell_index += 1

print(shell)