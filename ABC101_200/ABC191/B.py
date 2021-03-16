NX=input().split()
A=input().split()
N=NX[0]
X=NX[1]

ans=[]
for a in A:
    if(a==X):
        continue
    else:
        ans.append(a)

if(len(ans)>0):
    print(" ".join(ans))
else:
    print()