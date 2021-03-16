
N=int(input())

ans=10000000000
for i in range(N):
    a,p,x=map(int,input().split())
    if(x-a<=0):
        continue
    else:
        if(p<ans):
            ans=p

if(ans==10000000000):
    ans=-1

print(ans)