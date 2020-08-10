import sys

array = input().split()
new_array = [int(i) for i in array]
line = input()

def minF(seq):
    minNum = sys.maxsize
    for i in seq:
        if i < minNum:
            minNum = i
    return minNum

def maxF(seq):
    maxNum = -sys.maxsize
    for i in seq:
        if i > maxNum:
            maxNum = i
    return maxNum

def even(seq):
    pass
def odd(seq):
    pass

while line != "end":
    pair = line.split()
    if pair[0] == "exchange":
        indx = int(pair[1])
        arr1 = new_array[:indx]
        arr2 = new_array[indx:]
        arr2.extend(arr1)
        print(arr2)
    if pair[0] == "max":
        if pair[1] == "odd":
            pass
        if pair[1] == "even":
            pass

    if pair[0] == "min":
        if pair[1] == "odd":
            pass
        if pair[1] == "even":
            pass
    line = input()
