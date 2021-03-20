
N=int(input())

keta=len(str(N))

if(keta%2==0):
    pre=str(N)[:int(keta/2)]
else:
    pre=str(N)[:int(keta/2)+1]

ans=0
for x in range(1,int(pre)+1,1):
    strx=str(x)+str(x)
    numx=int(strx)

    if(numx<=N):
        ans+=1

print(ans)