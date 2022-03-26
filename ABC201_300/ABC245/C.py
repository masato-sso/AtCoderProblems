
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [False]*N
ep = [False]*N

for i in range(N):
    if(i == 0):
        dp[0] = True
        ep[0] = True
    
    if(dp[i - 1]):
        if(abs(A[i - 1] - A[i]) <= K):
            dp[i] = True
        if(abs(A[i - 1] - B[i]) <= K):
            ep[i] = True
    
    if(ep[i - 1]):
        if(abs(B[i - 1] - A[i]) <= K):
            dp[i] = True
        if(abs(B[i - 1] - B[i]) <= K):
            ep[i] = True

if(dp[N - 1] or ep[N - 1]):
    print("Yes")
else:
    print("No")
