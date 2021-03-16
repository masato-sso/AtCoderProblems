import numpy as np

K=int(input())
AB=np.array(input().split(" "),dtype=np.int32)
A=AB[0]
B=AB[1]

flag=False

for i in range(A,B+1):
    if(i%K==0):
        flag=True

if(flag):
    print("OK")
else:
    print("NG")

