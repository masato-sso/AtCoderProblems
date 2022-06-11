
N, K = map(int, input().split())
A = list(map(int, input().split()))
P = []
Q = []
for i in range(N):
    XY = [*map(int, input().split())]
    if(i + 1 in A):
        Q += [XY]
    else:
        P += [XY]

print(max(min((u-x)**2+(v-y)**2 for u,v in Q) for x,y in P)**.5)

    