the_string = input()
the_new_string = ""

for i in range(len(the_string)):
    if i + 1 == len(the_string):
        the_new_string += the_string[i]
        break
    if the_string[i] == the_string[i+1]:
        continue
    the_new_string += the_string[i]

print(the_new_string)