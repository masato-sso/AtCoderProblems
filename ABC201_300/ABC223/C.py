
N = int(input())
A = []
B = []
C = [] # time
time = 0
for i in range(N):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)
    tmp = float(a/b)
    C.append(tmp)
    time += tmp

hit_time = time/2.0

ans = 0
for i in range(N):
    ans += min(A[i], hit_time*B[i])
    hit_time -= min(C[i], hit_time)

print(ans)
