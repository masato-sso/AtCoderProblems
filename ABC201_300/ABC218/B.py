
P=list(map(int,input().split()))

alpha=list("abcdefghijklmnopqrstuvwxyz")

ans=""
for i in range(26):
    ans=ans+alpha[P[i]-1]

print(ans)