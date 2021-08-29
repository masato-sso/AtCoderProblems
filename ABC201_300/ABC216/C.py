
N=int(input())
tmp=N
ans=""
while(True):
    if(tmp==0):
        break
    if(tmp%2==0):
        tmp=tmp//2
        ans="B"+ans
    else:
        tmp=tmp-1
        ans="A"+ans

print(ans)