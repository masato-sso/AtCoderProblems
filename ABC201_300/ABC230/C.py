
N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

ans = []
board = "."*(S-R+1)

for i in range(0, Q-P+1):
    ans.append(list(board))

x = max(P-A, R-B)
y = min(Q-A, S-B)
for i in range(x, y+1):
    ans[A + i - P][B + i - R] = "#"

x = max(P-A, B-S)
y = min(Q-A, B-R)
for i in range(x, y+1):
    ans[A + i - P][B - i - R] = "#"

for i in range(0, Q-P+1):
    print("".join(ans[i]))
