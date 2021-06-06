
N=int(input())
A=list(map(int,input().split()))

s=0
for i in range(N):
    tmp=A[i]-10
    if(tmp>0):
        s+=tmp

print(s)