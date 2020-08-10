line = input()
import re
names = line.split()
user_name_pattern = r"([A-Za-z]*)([0-9]*)"

while line != "end of race":

    line = input()
    name = ""
    result = []
    result2 = ""
    name_new = re.findall(user_name_pattern, line)

    for runner_name in name_new:
        name += runner_name[0]
    print(name)

    for runner_result in name_new:
        result.append(runner_result[1])
        for i in result:
            if i.isdigit() != True:
                result.remove(i)
        result2 = "".join(result)

    result3 = 0
    for i in result2:
        result3 += int(i)
    print(result3)

