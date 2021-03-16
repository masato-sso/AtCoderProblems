import numpy as np

N=int(input())

D=[]

for i in range(N):
    D.append(np.array(input().split(" "),dtype=np.int64))

cnt=0
max_cnt=0
for i in range(N):
    if(D[i][0]==D[i][1]):
        cnt+=1
    else:
        if(cnt>max_cnt):
            max_cnt=cnt
        cnt=0

if(cnt>max_cnt):
    max_cnt=cnt

if(max_cnt>=3):
    print("Yes")
else:
    print("No")