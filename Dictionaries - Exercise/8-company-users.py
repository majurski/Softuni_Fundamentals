emp = input()

companies = {}

while emp != "End":
    line = emp.split(" -> ")
    companyName = line[0]
    employeeId = line[1]

    if companyName not in companies:
        companies[companyName] = []

    if employeeId not in companies[companyName]:
        companies[companyName].append(employeeId)

    emp = input()

companies = dict(sorted(companies.items(), key=lambda x: x[0]))
for k, v in companies.items():
    print(f"{k}")
    for st in v:
        print(f"-- {st}")