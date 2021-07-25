
S=input()

pattern="chokudai"
mod=10**9+7
dp=[[0 for i in range(len(pattern))] for j in range(len(S))] 

for i in range(len(S)):
    if(i>0):
        for j in range(len(pattern)):
            dp[i][j]=dp[i-1][j]
    if(S[i] in list(pattern)):
        j=list(pattern).index(S[i])
        if(j==0):
            dp[i][j]+=1
        else:
            dp[i][j]+=dp[i-1][j-1]
            dp[i][j]%=mod

print(dp[len(S)-1][len(pattern)-1]%mod)