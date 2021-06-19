
N=int(input())

day=1
flag=True
ans=-1
while(flag):
    if(day*(day+1)>=2*N):
        flag=False
        ans=day
        break
    day+=1

print(ans)