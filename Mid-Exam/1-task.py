employees_per_hour_1 = int(input())
employees_per_hour_2 = int(input())
employees_per_hour_3 = int(input())
number_of_students = int(input())

all_students_per_hour = employees_per_hour_1 + employees_per_hour_2 + employees_per_hour_3
count_hour = 0

while number_of_students > 0:
    number_of_students -= all_students_per_hour
    count_hour += 1
    if count_hour % 4 == 0:
        count_hour += 1


print(f"Time needed: {count_hour}h.")