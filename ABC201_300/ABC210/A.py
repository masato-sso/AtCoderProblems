
N,A,X,Y=map(int,input().split())

ans=0
cnt=N
if(N>A):
    ans+=X*A
    cnt=cnt-A
    ans+=cnt*Y
else:
    ans+=X*N

print(ans)