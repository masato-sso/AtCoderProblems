
N,X=map(int,input().split())
A=list(map(int,input().split()))

s=0
for i in range(N):
    idx=i+1
    if(idx%2==0):
        s+=A[i]-1
    else:
        s+=A[i]

if(s<=X):
    print("Yes")
else:
    print("No")
