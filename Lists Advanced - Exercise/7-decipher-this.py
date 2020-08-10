msg = input().split()

temp = []
cyp = []
for cypher in msg:
    for i in cypher:
        if i.isdigit():
            temp.append(i)
        else:
            cyp.append(i)
    ch = ''.join(temp)
    cyp.insert(0, chr(int(ch)))
    cyp[1], cyp[-1] = cyp[-1], cyp[1]
    end_word = ''.join(cyp)
    temp = []
    cyp = []
    print(end_word, end = " ")
