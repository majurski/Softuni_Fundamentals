def get_letter_pos_in_alphabet(letter):
    position = ord(letter) - 64

    if letter.islower():
        position = ord(letter) - 96


    return position

def calculate_leter_result(item):

    first_letter = item[0]
    last_letter = item[-1]
    number = int(item[1:-1])

    first_letter_position = get_letter_pos_in_alphabet(first_letter)
    last_letter_postion = get_letter_pos_in_alphabet(last_letter)

    res = 0

    if first_letter.isupper():
        res = number / first_letter_position
    else:
        res = number * first_letter_position

    if last_letter.isupper():
        res -= last_letter_postion
    else:
        res+= last_letter_postion

    return res

items = input().split()
total = 0

for item in items:
    res = calculate_leter_result(item)
    total += res
print(f"{total:.2f}")