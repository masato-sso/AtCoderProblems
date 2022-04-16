
N, M, K = map(int, input().split())

MOD =  998244353

dp = [[0 for i in range(K)] for _ in range(N)]

for i in range(N):
    if(i == 0):
        for j in range(M):
            dp[i][j] = 1
    else:
        for k in range(K):
            c = 0
            for j in range(max(0, k - M), k):
                c += dp[i - 1][j] % MOD
            dp[i][k] = c

print(sum(dp[-1])%MOD)
