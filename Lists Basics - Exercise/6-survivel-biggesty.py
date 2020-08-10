import sys
min_num = sys.maxsize
ls = input().split(" ")
lss = [int(i) for i in ls]
nums = int(input())

for i in range(nums):
    for b in lss:
        if b < min_num:
            min_num = b
    if min_num in lss:
        lss.remove(min_num)
        min_num = sys.maxsize

print(lss)










