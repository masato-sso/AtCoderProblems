
N, M, X, T, D = map(int, input().split())

ans = T
for age in range(N, -1, -1):
    if(X<=age and age<=N):
        ans = ans
    else:
        ans = ans - D
    if(M == age):
        break

print(ans)