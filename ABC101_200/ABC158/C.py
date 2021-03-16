import numpy as np

AB=np.array(input().split(" "),dtype=np.int32)

A=AB[0]
B=AB[1]

canA=A/0.08
canB=B/0.1

start=0
if(canA<canB):
    start=canA
else:
    start=canB

ans=-1
th=2*start
while (True):
    outA=int(start*0.08)
    outB=int(start*0.10)
    if(outA==A and outB==B):
        ans=start
        break
    if(start>2*th):
        break
    start+=1

print(int(ans))