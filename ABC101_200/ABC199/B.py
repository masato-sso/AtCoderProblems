
N=int(input())

A=list(map(int,input().split()))
B=list(map(int,input().split()))

lower=max(A)
higher=min(B)

ans=higher-lower+1

if(ans<0):
    ans=0

print(ans)