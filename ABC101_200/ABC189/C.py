
N=int(input())
A = list(map(int, input().split()))

ans=0

for l in range(N):
    tmp=A[l]
    for r in range(l,N):
        tmp=min(tmp,A[r])
        ans=max(ans,tmp*(r-l+1))

print(ans)
