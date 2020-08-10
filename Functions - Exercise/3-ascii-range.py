char1 = input()
char2 = input()

def between(char1, char2):
    for i in range(int(ord(char1))+1, int(ord(char2))) :
        print(chr(i), end = " ")

between(char1,char2)