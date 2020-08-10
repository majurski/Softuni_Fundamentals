num = input()

def even_odd(num):
    even = 0
    odd = 0
    for i in num:
        if int(i) % 2 == 0:
            even += int(i)
        else:
            odd += int(i)

    return f"Odd sum = {odd}, Even sum = {even}"

print(even_odd(num))
