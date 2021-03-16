h,w = map(int,input().split())
S = []
for i in range(h):
    si = input()
    S.append(si)
ans = 0
for i in range(h-1):
    for j in range(w-1):
        k = 0
        if S[i][j] == "#":
            k += 1
        if S[i][j+1] == "#":
            k += 1
        if S[i+1][j] == "#":
            k += 1
        if S[i+1][j+1] == "#":
            k += 1
        if k == 1 or k == 3:
            ans += 1
print(ans)
