
N = int(input())

S = []
for i in range(N):
    S.append(input())

ans = S[::-1]
for i in range(N):
    print(ans[i])