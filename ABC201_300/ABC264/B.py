
R, C = map(int, input().split())

block = []
for i in range(1, 16):
    tmp = []
    for j in range(1, 16):
        if(i == 2 and 1 < j and j < 15):
            tmp.append("white")
        elif(i == 4 and 3 < j and j < 13):
            tmp.append("white")
        elif(i == 6 and 5 < j and j < 11):
            tmp.append("white")
        elif(i == 8 and j == 8):
            tmp.append("white")
        elif(i == 10 and 5 < j and j < 11):
            tmp.append("white")
        elif(i == 12 and 3 < j and j < 13):
            tmp.append("white")
        elif(i == 14 and 1 < j and j < 15):
            tmp.append("white")
        elif(1 < i and i < 15 and j == 2):
            tmp.append("white")
        elif(3 < i and i < 13 and j == 4):
            tmp.append("white")
        elif(5 < i and i < 11 and j == 6):
            tmp.append("white")
        elif(5 < i and i < 11 and j == 10):
            tmp.append("white")
        elif(3 < i and i < 13 and j == 12):
            tmp.append("white")
        elif(1 < i and i < 15 and j == 14):
            tmp.append("white")
        else:
            tmp.append("black")
    block.append(tmp)

R = R - 1
C = C - 1
print(block[R][C])