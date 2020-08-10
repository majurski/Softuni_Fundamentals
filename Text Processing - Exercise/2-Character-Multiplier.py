line = input().split()

first_word = line[0]
second_word = line[1]

min_value = min(len(first_word), len(second_word))

all_sum = 0

for i in range(min_value):
    result = ord(first_word[i]) * ord(second_word[i])
    all_sum += result

longest_word = first_word

if len(second_word) > len(first_word):
    longest_word = second_word

for i in range(min_value, len(longest_word)):
    all_sum += ord(longest_word[i])

print(all_sum)