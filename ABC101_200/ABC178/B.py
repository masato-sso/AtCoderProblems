import numpy as np

abcd=np.array(input().split(" "),dtype=np.int64)
a=abcd[0]
b=abcd[1]
c=abcd[2]
d=abcd[3]

can=[a*c,a*d,b*c,b*d]

print(max(can))