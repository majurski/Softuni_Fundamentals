num1 = int(input())
num2 = int(input())

def fact_func(num):
    for i in range(1, num):
        num = num * i
    return num

def division_func(num1, num2):
    res = fact_func(num1) / fact_func(num2)
    print(f"{res:.2f}")

division_func(num1, num2)