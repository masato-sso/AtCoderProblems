import numpy as np

AB=np.array(input().split(" "),dtype=np.int64)

A=AB[0]
B=AB[1]

follow=2*A+100

print(follow-B)