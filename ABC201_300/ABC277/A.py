
N, X = map(int, input().split())
P = list(map(int, input().split()))

for idx in range(N):
    if(P[idx] == X):
        print(idx + 1)
        break
