the_string = input()
result = 0

i = 0
while i < len(the_string):
    ch = the_string[i]

    if ch == ">":
        result += int(the_string[i + 1])
    else:
        if result > 0:
            the_string = the_string[:i] + the_string[i + 1:]
            i -= 1
            result -= 1
    i += 1
print(the_string)