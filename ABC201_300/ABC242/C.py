
N = int(input())

MOD = 998244353
dp = []

for i in range(9):
    dp.append([1]*N)

s = 0
for i in range(1,N):
    for j in range(9):
        if(j == 0):
            s = dp[j][i-1] + dp[j+1][i-1]
        elif(j == 8):
            s = dp[j-1][i-1] + dp[j][i-1]
        else:
            s = dp[j-1][i-1] + dp[j][i-1] + dp[j+1][i-1]
        dp[j][i] = s%MOD

ans = 0
for j in range(9):
    ans += dp[j][-1]
ans = ans%MOD

print(ans)