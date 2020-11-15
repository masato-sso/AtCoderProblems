import numpy as np

SG=np.array(input().split(" "),dtype=np.int64)
S=[SG[0],SG[1]]
G=[SG[2],SG[3]]

up=float(S[1]*G[0]+G[1]*S[0])
down=float(S[1]+G[1])
ans=float(up/down)
print(ans)