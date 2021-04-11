
N=int(input())

ans=0

for a in range(1,N+1):
    b=N-a
    if(b<=0):
        continue
    else:
        ans+=1

print(ans)