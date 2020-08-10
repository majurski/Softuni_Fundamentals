num = int(input())

for i in range(0, num):
    for j in range(0, num):
        for m in range(0, num):
            q = chr(97 + i)
            w = chr(97 + j)
            s = chr(97 + m)
            print(f"{q}{w}{s}")