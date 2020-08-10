rooms = int(input())
number_room = 0
free_chairs = 0
is_ready = True

while rooms > 0:
    rooms -= 1
    number_room += 1
    pair = input().split()
    chair = int(len(pair[0]))
    people = int(pair[1])
    if chair > people:
        free_chairs += (chair - people)
    elif chair < people:
        is_ready = False
        missing_chairs = 0
        missing_chairs += (people - chair)
        print(f"{missing_chairs} more chairs needed in room {number_room}")

if is_ready:
    print(f"Game On, {free_chairs} free chairs left")