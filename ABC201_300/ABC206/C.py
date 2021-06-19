import collections

N=int(input())
A=list(map(int,input().split()))

c = collections.Counter(A)

remains=N-1
ans=0
for idx in range(N-1):
    a=A[idx]
    cnt=c[a]
    if(cnt>=2):
        tmp=remains-cnt+1
        if(tmp>0):
            ans+=tmp
    elif(cnt==1):
        ans+=remains
    c[a]=c[a]-1
    remains=remains-1

print(ans)