str1 = input().split(", ")
str2 = input().split(", ")
end = []


for i in str1:
    for b in str2:
        if i in b:
            if i in end:
                pass
            else:
                end.append(i)

print(end)