def is_palindrome(text):
    mid_index = len(text) // 2
    end_index = len(text) - 1

    for i in range(mid_index):
        if text[i] != text[end_index - i]:
            return False
        else:
            return True


text = input().split(", ")
for b in text:
    if len(b) == 1:
        print(True)
    else:
        print(is_palindrome(b))
