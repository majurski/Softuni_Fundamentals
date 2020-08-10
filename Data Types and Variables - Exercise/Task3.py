import math
persons = int(input())
capacity = int(input())


if capacity > persons:
    print(1)
else:
    ends = persons // capacity
    check = persons % capacity
    if check > 0:
        print(ends + 1)
    else:
        print(ends)

