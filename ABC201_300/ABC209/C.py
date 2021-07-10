
N=int(input())
C=list(map(int,input().split()))

MOD=1000000000+7
sortedC=sorted(C)

ans=0
done=0
select=1
for i in range(N):
    can=sortedC[i]%MOD-done
    if(can<0):
        can=0
    select=select*can
    select=select%MOD
    done+=1

if(select<0):
    ans=0
else:
    ans=select

ans=ans%MOD
print(ans)