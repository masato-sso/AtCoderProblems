import numpy as np

HWK=np.array(input().split(" "),dtype=np.int64)
H=HWK[0]
W=HWK[1]
K=HWK[2]

C=[]
for i in range(H):
    C.append(list(input()))

count=0

for maskR in range((1<<H)):
    for maskC in range((1<<W)):
        black=0
        for i in range(H):
            for j in range(W):
                if(((maskR>>i)&1)==0) and (((maskC>>j)&1)==0) and C[i][j]=="#":
                    black+=1
        if(black==K):
            count+=1

print(count)