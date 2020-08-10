def pass_check(text):
    digits = 0
    letter = 0
    val_pass = True
    if len(text) < 6 or len(text) > 10:
        print(f"Password must be between 6 and 10 characters")
        val_pass = False

    for i in text:
        if i.isdigit():
            digits += 1
        if i.isalpha():
            letter += 1
    if digits + letter != len(text):
        print(f"Password must consist only of letters and digits")
        val_pass = False

    if digits < 2:
        print(f"Password must have at least 2 digits")
        val_pass = False
    if val_pass:
        print(f"Password is valid")

word = input()
pass_check(word)

