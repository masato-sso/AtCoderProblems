import numpy as np

AB=np.array(input().split(" "),dtype=np.int64)
CD=np.array(input().split(" "),dtype=np.int64)

a=AB[0]
b=AB[1]
c=CD[0]
d=CD[1]

ans=a*d-b*c
print(ans)
