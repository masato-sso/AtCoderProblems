
N = int(input())
T = input()

x,y = 0,0

cnt = 0
for i in range(N):
    t = T[i]
    cnt = cnt%4
    if(t == "S"):
        if(cnt == 0):
            x += 1
        elif(cnt == 1):
            y -= 1
        elif(cnt == 2):
            x -= 1
        else:
            y += 1
    else:
        cnt += 1

print("{} {}".format(x,y))
