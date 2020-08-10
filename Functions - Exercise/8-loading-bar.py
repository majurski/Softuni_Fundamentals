load = int(input())

if load < 100:
    loader = 10 * ["."]
    m = load // 10
    for i in range(m):
        loader[i] = "%"
    last = ''
    last = last.join(loader)
    print(f"{m*10}% [{last}]")
    print(f"Still loading...")
else:
    print(f"100% Complete!")
    print(f"[%%%%%%%%%%]")
