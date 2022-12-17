
N, M = map(int, input().split())
S = []
for i in range(N):
    S.append(input())

ans = 0
for i in range(N):
    for k in range(i+1,N):
        flag = True
        for j in range(M):
            if(S[i][j] == "x" and S[k][j] == "x"):
                flag = False
                continue
        if(flag):
            ans += 1

print(ans)