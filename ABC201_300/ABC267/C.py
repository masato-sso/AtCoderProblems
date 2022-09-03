
N, M = map(int, input().split())
A = list(map(int, input().split()))

s = [0]*(N + 1)
for i in range(1, N + 1):
    s[i] = s[i - 1] + A[i - 1]

now = 0
for i in range(M):
    now += A[i]*(i + 1)

result = [0] * (N - M + 1)
result[0] = now
for i in range(1, N - M + 1):
    result[i] = result[i - 1] + M*A[M + i - 1] - (s[M + i - 1] - s[i - 1])

ans = -1000000000000000000
for i in range(N - M + 1):
    ans = max(ans, result[i])

print(ans)