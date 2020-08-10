import sys
divisor = int(input())
bound = int(input())
n = 0
maxNum = -sys.maxsize
while n <= bound:
    n += 1
    if n % divisor == 0 and n <= bound:
        maxNum = n

print(maxNum)
