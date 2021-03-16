
N=int(input())
sA=input().split(" ")
A=[]

for i in range(N):
    A.append(int(sA[i]))

flag=False

zero=False
th=pow(10,18)
for i in range(N):
    if(A[i]==0):
        zero=True
        break
    elif(A[i]>th):
        flag=True
        break

S=1
for i in range(N):
    S*=A[i]
    if(S>th):
        flag=True
        break

if(zero):
    print(0)
else:
    if(flag):
        print(-1)
    else:
        print(S)
