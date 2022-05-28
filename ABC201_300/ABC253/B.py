
H, W = map(int, input().split())
S = []
for i in range(H):
    S.append(input())

px1 = 0
py1 = 0
px2 = 0
py2 = 0
cnt = 0
for h in range(H):
    for w in range(W):
        if(S[h][w] == "o"):
            if(cnt == 0):
                px1 = h
                py1 = w
                cnt += 1
            else:
                px2 = h
                py2 = w

ans = abs(px1 - px2) + abs(py1 - py2)

print(ans)
