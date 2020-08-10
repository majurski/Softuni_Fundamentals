text = input()
new_word = ""
for i in range(len(text)):
    symb = ord(text[i])
    new_sym = chr(symb+3)
    new_word += new_sym
print(new_word)
