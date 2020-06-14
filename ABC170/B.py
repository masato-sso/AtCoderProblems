import numpy as np

XY=np.array(input().split(" "),dtype=np.int32)

X=XY[0]
Y=XY[1]

b_count=0
t_count=0

flag=False
for x in range(X+1):
    b_count=x
    t_count=X-b_count

    legs=2*b_count+4*t_count

    if(legs==Y):
        flag=True
        break

if(flag):
    print("Yes")
else:
    print("No")
