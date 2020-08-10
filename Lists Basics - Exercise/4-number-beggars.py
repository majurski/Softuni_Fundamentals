nums = input().split(", ")
beggars = int(input())

beggars_list = [0 for i in range(0, beggars)]
count = 0

for i in nums:
    beggars_list[count] = int(beggars_list[count]) + int(i)
    count += 1
    if count == beggars:
        count = 0
print(beggars_list)