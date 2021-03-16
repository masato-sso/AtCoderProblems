
X=int(input())

mod=X%100

ans=0
if(mod==0):
    ans=100
else:
    ans=100-mod

print(ans)