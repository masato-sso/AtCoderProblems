import numpy as np

H,W = map(int, input().split())
A = []
for i in range(H):
    A.append(list(map(str, input().split())))

A = np.array(A)
B = A.T

ans = ""
for h in range(W): 
    ans = ans + " ".join(B[h])
    ans = ans + "\n"
 
print(ans)