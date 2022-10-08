import itertools
from re import T

N, M = map(int, input().split())
X = []
for i in range(M):
    kx = list(map(int, input().split()))
    X.append(kx[1:])

cands = list(itertools.combinations(range(1, N + 1), 2))

ans = True
for can in cands:
    target = list(can)
    ret = 0
    for x in X:
        find = True
        for tar in target:
            if(tar in x):
                continue
            find = False
        if(find):
            ret = 1
            break
    if(ret):
        continue
    ans = False
    break

if(ans):
    print("Yes")
else:
    print("No")