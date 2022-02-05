
N = int(input())

MOD = 998244353

ans = 0
l = 1
for i in range(len(str(N))):
    if (i < len(str(N)) - 1):
        r = l * 10
    else:
        r = N + 1
    n = r - l
    ans += n*(n+1)//2
    ans %= MOD
    l = r

print(int(ans))