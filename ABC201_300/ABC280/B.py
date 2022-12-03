
N = int(input())
S = list(map(int, input().split()))

sumS = [S[0]]
result = [S[0]]
for i in range(1, N):
    s = S[i]
    result.append(S[i] - sumS[i - 1])
    sumS.append(sum(result))

print(*result)