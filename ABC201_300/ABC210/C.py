from collections import Counter

N, K = map(int,input().split())
c=list(map(int,input().split()))
counter=Counter(c[:K])

t=len(counter)
ans=t

for l,r in zip(c,c[K:]):
    t+=(counter[r]<1)
    counter[r]+=1
    counter[l]-=1
    t-=(counter[l]<1)
    ans=max(ans,t)

print(ans)