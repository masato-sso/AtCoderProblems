
N=int(input())

ans=0

if(N>125):
    if(N>211):
        ans=8
    else:
        ans=6
else:
    ans=4

print(ans)