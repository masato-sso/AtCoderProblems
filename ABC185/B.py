import numpy as np

NMT=np.array(input().split(" "),dtype=np.int64)
N=NMT[0]
M=NMT[1]
T=NMT[2]

AB=[]
for i in range(M):
    AB.append(np.array(input().split(" "),dtype=np.int64))


battery=N
t=0
zero_flag=False
for i in range(M):
    use=(AB[i][0]-t)
    accum=(AB[i][1]-AB[i][0])
    battery=battery-use
    if(battery<=0):
        zero_flag=True
    if(battery+accum>=N):
        battery=N
    else:
        battery=battery+accum
    t=AB[i][1]
    if(battery<=0):
        zero_flag=True

use=(T-t)
battery=battery-use

if(zero_flag):
    print("No")
else:
    if(battery>0):
        print("Yes")
    else:
        print("No")
