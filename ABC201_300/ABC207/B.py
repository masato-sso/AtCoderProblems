import math

A,B,C,D=map(int,input().split())

ans=-1

diff=C*D-B
if(diff!=0):
    ans=math.ceil(A/(diff))
    if(ans<0):
        ans=-1

print(ans)