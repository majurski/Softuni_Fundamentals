the_string = input()

for i in range(len(the_string)):
    if the_string[i] == ":":
        print(the_string[i]+the_string[i+1])