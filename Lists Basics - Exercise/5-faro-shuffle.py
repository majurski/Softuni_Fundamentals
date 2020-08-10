cards = input().split(" ")
nums = int(input())
half_index = int(len(cards) // 2)

for c in range(nums):
    temp_cont = []
    for i in range(half_index):
        first_card = cards[i]
        sec_card_index = i + half_index
        sec_card = cards[sec_card_index]
        temp_cont.append(first_card)
        temp_cont.append(sec_card)
    cards = temp_cont

print(cards)




