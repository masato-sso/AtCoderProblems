
H,W,X,Y=map(int,input().split())

S=[]
for i in range(H):
    S.append(input())

ans=0
X=X-1
Y=Y-1

up=X-1
for h in range(H):
    if(up>=0):
        if(S[up][Y]=="."):
            ans+=1
        else:
            break
    else:
        break
    up=up-1

down=X+1 
for h in range(H):
    if(down<H):
        if(S[down][Y]=="."):
            ans+=1
        else:
            break
    else:
        break
    down=down+1

left=Y-1
for w in range(W):
    if(left>=0):
        if(S[X][left]=="."):
            ans+=1
        else:
            break
    else:
        break
    left=left-1

right=Y+1
for w in range(W):
    if(right<W):
        if(S[X][right]=="."):
            ans+=1
        else:
            break
    else:
        break
    right=right+1

if(S[X][Y]=="."):
    ans+=1

print(ans)
