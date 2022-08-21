
H, W = map(int, input().split())
G = []
for i in range(H):
    tmp = list(input())
    line = []
    for t in tmp:
        line.append([t, True])
    G.append(line)

x = 0
y = 0

clearFlag = True
while(True):
    move = G[x][y][0]
    if(not(G[x][y][1])):
        clearFlag = False
        break
    G[x][y][1] = False
    if(move == "U"):
        if(x != 0):
            x = x - 1
        else:
            break
    elif(move == "D"):
        if(x != H - 1):
            x = x + 1
        else:
            break
    elif(move == "L"):
        if(y != 0):
            y = y - 1
        else:
            break
    elif(move == "R"):
        if(y != W - 1):
            y = y + 1
        else:
            break

if(not(clearFlag)):
    print(-1)
else:
    print("{} {}".format(x + 1, y + 1))