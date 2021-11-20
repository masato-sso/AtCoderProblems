
N,K = map(int, input().split())
P = []
for i in range(N):
    P.append(list(map(int, input().split())))

S = []
for p in P:
    S.append(sum(p))

k_score = sorted(S)[::-1][K-1]
for x in S:
    if(k_score > x +300 ):
        print("No")
    else:
        print("Yes")
