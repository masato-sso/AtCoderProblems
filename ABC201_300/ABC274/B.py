
H, W = map(int, input().split())
C = []
for h in range(H):
    line = input()
    C.append(line)

X = []

for w in range(W):
    cnt = 0
    for h in range(H):
        val = C[h][w]
        if(val == "#"):
            cnt += 1
    X.append(str(cnt))

print(" ".join(X))