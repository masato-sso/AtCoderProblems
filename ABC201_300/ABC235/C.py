
from collections import defaultdict

N, Q = map(int, input().split())
A = list(map(int, input().split()))
xk = []
for i in range(Q):
    x,k = map(int, input().split())
    xk.append([x, k])

dic = defaultdict(list)
for i in range(len(A)):
    dic[A[i]].append(i)

for i in range(len(xk)):
    x = xk[i][0]
    k = xk[i][1]

    idxes = dic[x]
    length = len(idxes)
    if(length < k):
        print(-1)
    else:
        print(idxes[k - 1] + 1)
