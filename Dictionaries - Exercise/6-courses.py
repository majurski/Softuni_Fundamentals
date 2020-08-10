items = input()

courses = {}

while items != "end":
    prods = items.split(" : ")
    course = prods[0]
    name = prods[1]

    if course not in courses:
        courses[course] = []

    courses[course].append(name)

    items = input()

sorted_courses = dict(sorted(courses.items(), key=lambda x: len(x[1]), reverse=True))

for k,v in sorted_courses.items():
    print(f"{k}: {len(v)}")

    for student_name in sorted(v):
        print(f"-- {student_name}")