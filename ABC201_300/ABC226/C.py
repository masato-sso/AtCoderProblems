
N = int(input())
T = []
K = []
A = []
for i in range(N):
    S = list(map(int,input().split()))
    T.append(S[0])
    K.append(S[1])
    A.append(S[2:])

used = [0]*N
used[N-1] = 1
times = 0
for i in range(N-1,-1,-1):
    if(used[i]):
        times += T[i]
        for a in A[i]:
            used[a-1] = 1

print(times)