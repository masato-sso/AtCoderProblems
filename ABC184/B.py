
NX=input().split(" ")
S=input()

N=int(NX[0])
X=int(NX[1])

ans=X
for s in S:
    if(s=="o"):
        ans+=1
    else:
        ans-=1
    if(ans<0):
        ans=0

print(ans)
