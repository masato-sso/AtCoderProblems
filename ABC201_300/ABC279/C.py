
H, W = map(int, input().split())
S = [[0 for i in range(H)] for j in range(W)]
T = [[0 for i in range(H)] for j in range(W)]

for i in range(H):
    s = input()
    for j in range(W):
        S[j][i] = s[j]

for i in range(H):
    t = input()
    for j in range(W):
        T[j][i] = t[j]

S.sort()
T.sort()

if(S != T):
    print("No")
    exit(0)

print("Yes")