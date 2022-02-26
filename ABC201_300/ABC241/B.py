import collections

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

Acounter = collections.Counter(A)
Bcounter = collections.Counter(B)

setB = list(set(B))
flag = True
for b in setB:
    if(Acounter[b] < Bcounter[b]):
        flag = False
        break

if(flag):
    print("Yes")
else:
    print("No")
