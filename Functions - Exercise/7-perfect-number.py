num = int(input())
half = num//2
cont = []

def check_nice_num(num):
    for i in range(1, half):
        if num % i == 0:
            cont.append(i)
    if sum(cont)*2 == num:
        print(f"We have a perfect number!")
    else:
        print(f"It's not so perfect.")

check_nice_num(num)
