
N = int(input())
A = []
for i in range(N):
    a = list(map(int, list(input())))
    A.append(a)

p = [1,1,1,0,0,-1,-1,-1]
q = [1,0,-1,1,-1,1,0,-1]

ans = 0
for i in range(N):
    for j in range(N):
        for k in range(8):
            now = 0
            x = i
            y = j
            for l in range(N):
                now *= 10
                now += A[x][y]
                x += p[k]
                y += q[k]
                x %= N
                y %= N
            ans = max(ans, now)

print(ans)
