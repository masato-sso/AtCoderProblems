import numpy as np

A1=np.array(input().split(" "),dtype=np.int32)
A2=np.array(input().split(" "),dtype=np.int32)
A3=np.array(input().split(" "),dtype=np.int32)

A=[A1,A2,A3]

N=int(input())

B=[]
for i in range(N):
    B.append(int(input()))

T=np.zeros((3,3),dtype=np.int32)

for n in range(N):
    value=B[n]
    for i in range(3):
        for j in range(3):
            if(value==A[i][j]):
                T[i][j]=1

# horizontal
flag=False
for i in range(3):
    cnt=0
    for j in range(3):
        if(T[i][j]==0):
            break
        else:
            cnt+=1
    if(cnt==3):
        flag=True

# vertical
for i in range(3):
    cnt=0
    for j in range(3):
        if(T[j][i]==0):
            break
        else:
            cnt+=1
    if(cnt==3):
        flag=True

if(T[0][0]==1 and T[1][1]==1 and T[2][2]==1):
    flag=True
elif(T[0][2]==1 and T[1][1]==1 and T[2][0]==1):
    flag=True

if(flag):
    print("Yes")
else:
    print("No")
