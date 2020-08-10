file_name = input()

b = ""
exten = ""
indx = -1

while b != ".":
    b = file_name[indx]
    exten += b
    indx -= 1

file_name = file_name[:-len(exten)]

c = ""
new_exten = ""
indx2 = -1

while c != "\\":
    c = file_name[indx2]
    new_exten += c
    indx2 -= 1

last_file_name = "".join(list(reversed(new_exten)))[1:]
file_ext = "".join(list(reversed(exten)))[1:]

print(f"File name: {last_file_name}")
print(f"File extension: {file_ext}")
