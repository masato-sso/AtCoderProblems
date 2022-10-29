import itertools

S = []
for i in range(9):
    S.append(input())

ans = 0
for y1, x1, y2, x2 in itertools.product(range(9), repeat=4):
    if((y1 < y2) and (x1<=x2) and S[y1][x1] == "#" and S[y2][x2] == "#"):
        dy = y2 - y1
        dx = x2 - x1
        y3 = y2 + dx
        x3 = x2 - dy
        y4 = y3 - dy
        x4 = x3 - dx
        if(-1 < y3 < 9 and -1 < x3 < 9 and -1 < y4 < 9 and -1 < x4 < 9):
            if(S[y3][x3] == "#" and S[y4][x4] == "#"):
                ans += 1

print(ans)
